# src\remittances\infraestructure\web\entrypoints\frontend_blueprint.py

from typing import Dict
from flask import Blueprint, jsonify, request
from src.remittances.application.services.customer_service import CustomerServiceApplication
from src.remittances.infraestructure.persistence.adapters.customer_persistence_adapter import CustomerRepositoryAdapter
from src.remittances.infraestructure.persistence.database.services.customer_orm_service import CustomerORMService
from src.shared.adapters.backen_platform_adapter import BackendPlatformAdapter
from src.shared.services.user_service import UserService
from src.shared.tools.auth.access import login_required

bp_frontend = Blueprint('frontend', __name__)

token_endpoint = '/customer/token'


@bp_frontend.route(token_endpoint, methods=["GET"], strict_slashes=False)
@login_required(user_info=True)
def get_token(user: dict):

    try:
        customer_orm_service = CustomerORMService()
        customer_repository = CustomerRepositoryAdapter(customer_orm_service)
        customer_application_service = CustomerServiceApplication(user.get('data'), customer_repository)
        token = customer_application_service.get_by_user_id()
        return jsonify({
            'statusCode': 200,
            'data': {
                'token': token
            }
        }), 200
    except Exception as e:
        return jsonify({
            'statusCode': 500,
            'data': {
                'message': str(e)
            }
        }), 500
    


@bp_frontend.route(token_endpoint, methods=["POST"], strict_slashes=False)
@login_required(user_info=False)
def set_token(user: dict):

    try:
        data = request.get_json()
        customer_orm_service = CustomerORMService()
        customer_repository = CustomerRepositoryAdapter(customer_orm_service)
        backend_adapter = BackendPlatformAdapter()
        user_service = UserService(backend_adapter)
        customer_application_service = CustomerServiceApplication(
            user_data=user.get('data'), 
            customer_repository=customer_repository,
            user_service=user_service
        )
        
        customer_application_service.save_token(token=data.get('token'))
        
        return jsonify({
            'statusCode': 200,
            'data': {
                'message': 'OK'
            }
        }), 200
    except Exception as e:
        return jsonify({
            'statusCode': 500,
            'data': {
                'message': str(e)
            }
        }), 500
        

    