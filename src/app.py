from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from redis import Redis
from flask_migrate import Migrate

from src.shared.ddd.domain.model.DomainEventPublisher import DomainEventPublisher
from src.shared.tools.errors.error_handler import constructor_error_handler

from src.name_service.application.subscribers.sample_subscriber import SampleSubscriber
from src.name_service.infraestructure.persistence.adapters.sample_persistence_adapter import SampleRepositoryAdapter
from src.name_service.infraestructure.persistence.database.services.sample_orm_service import SampleORMService
from src.name_service.infraestructure.persistence.database.instance import database_instance as db
from src.name_service.infraestructure.web.entrypoints import (
    sample_blueprint
)
from src.config.constants import PASS_SALT_NAME, SALT_KEY_NAME
from src.shared.cache.redis import RedisSingleton
from src.shared.tools.errors.method_not_allowed import send_method_not_found
from src.shared.tools.errors.not_found_handler import send_not_found


template_folder = 'context/infraestructure/endpoints/templates'
bps = (
    sample_blueprint.bp_sample,
)



def create_app(**kwargs):

    # templates
    app = Flask(
        __name__, template_folder=template_folder)


    # Load configurations from CONFIG
    app.config.from_mapping(**kwargs)

    db.init_app(app)

    app.config[SALT_KEY_NAME] = kwargs[PASS_SALT_NAME], kwargs['SECRET_KEY']



    app.redis = RedisSingleton(
        dns=kwargs["REDIS_DNS"], port=kwargs["REDIS_PORT"], database=kwargs["REDIS_DATABASE"]
    )

    # migrate = 
    Migrate(app, db)

    # Initialize Flask extensions
    app.config['bcrypt'] = Bcrypt(app)


    ################################### Add subscribers ###################################
    subcribers = (SampleSubscriber(SampleRepositoryAdapter(SampleORMService())),)
    [DomainEventPublisher.of().subscribe(
        subscribers=subscriber) for subscriber in subcribers]

    CORS(app)

    with app.app_context():


        [app.register_blueprint(
            blueprint=bp, url_prefix=kwargs["ROOT"]) for bp in bps]

        app.register_error_handler(
            code_or_exception=Exception,
            f=constructor_error_handler(logger=app.logger),
        )
        app.register_error_handler(code_or_exception=404, f=send_not_found)
        app.register_error_handler(
            code_or_exception=405, f=send_method_not_found)

        for rule in app.url_map.iter_rules():
            if rule.endpoint != 'static':
                print(rule)

        if __name__ == "__main__":
            app.run(
                host='0.0.0.0',
                threaded=True,
                port=kwargs["PORT"],
                debug=kwargs["DEBUG"],
            )

        return app
