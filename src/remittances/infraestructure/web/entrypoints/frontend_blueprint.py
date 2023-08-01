# src\remittances\infraestructure\web\entrypoints\frontend_blueprint.py

from typing import Dict
from flask import Blueprint, jsonify
from src.remittances.application.services.customer_service import CustomerServiceApplication
from src.remittances.infraestructure.persistence.adapters.customer_persistence_adapter import CustomerRepositoryAdapter
from src.remittances.infraestructure.persistence.database.services.customer_orm_service import CustomerORMService
from src.shared.tools.auth.access import login_required

bp_frontend = Blueprint('frontend', __name__)

token_endpoint = '/customer/token'

{
    "amount": "50000", 
    "name": "Nombre Contacto", 
    "phone": "9876543210", 
    "email": "cpinacho@multikrd.com"
}

@bp_frontend.route(token_endpoint, methods=["GET"], strict_slashes=False)
@login_required(user_info=True)
def token(user: dict):

    try:
        customer_orm_service = CustomerORMService()
        customer_repository = CustomerRepositoryAdapter(customer_orm_service)
        data = Dict(user.get('data'))
        user_data = {
            'user_id': data.get('id'),
            'name': f"{data.get('firstName')} {data.get('lastName')}",
            'email': data.get('email'),
            'phone': data.get('phone'),
        }
        customer_application_service = CustomerServiceApplication(user_data, customer_repository)
        token = customer_application_service.get_by_user()
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
    

    