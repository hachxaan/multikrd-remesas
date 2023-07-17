import re

from sqlalchemy.exc import IntegrityError

from src.name_service.infraestructure.persistence.database.instance import database_instance as db
from src.shared.tools.errors.project_exception import ProjectException
from src.shared.tools.logger import internal_logger

logger = internal_logger.get_logger()


class MetaService:
    @classmethod  # noqa: C901
    def commit(cls, entity: db.Model = None):
        try:
            if entity:
                db.session.add(entity)
            db.session.commit()

        except IntegrityError as e:
            """sqlalchemy.exc.IntegrityError"""
            matches = re.findall(
                r"(?<=Key \()[a-z_]*", e.orig.diag.message_detail)
            if matches:
                match = matches[0].replace('_id', '')
                if 'not present' in e.orig.diag.message_detail:
                    raise ProjectException(tag=f'{match.upper()}_NOT_FOUND',
                                           dynamic_error=dict(code=404, message=e.orig.diag.message_detail))
                elif 'already exists' in e.orig.diag.message_detail:
                    raise ProjectException(tag=f'{match.upper()}_ALREADY_EXISTING',
                                           dynamic_error=dict(code=409, message=f'{match} already existing'))
                else:
                    raise
            elif 'violates not-null constraint' in e.orig.diag.message_primary:
                matches = re.findall(
                    r"(?<=column )[\"a-z_]*", e.orig.diag.message_primary)
                if matches:
                    raise ProjectException(tag="VIOLATES_NOT_NULL_CONSTRAIN",
                                           message=f'the {matches[0]} violates not-null constraint')
            elif e.orig.pgcode == '23505':
                if 'name' in str(e.__dict__['orig']):
                    raise ProjectException(tag='EXISTING_NAME')
            else:
                # TODO catch other constrainsS
                raise e
        except Exception as e:
            logger.error(e)
            raise e
