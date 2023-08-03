# src\remittances\infraestructure\web\entrypoints\ria_blueprint.py

from flask import Blueprint, jsonify, request
from src.remittances.application.services.transfer_service import TransferServiceApplication
from src.remittances.infraestructure.exceptions.AccessDeniedException import AccessDeniedException
from src.remittances.infraestructure.persistence.adapters.customer_persistence_adapter import CustomerRepositoryAdapter
from src.remittances.infraestructure.persistence.database.services.customer_orm_service import CustomerORMService
from src.remittances.infraestructure.rest.adapters.transfer_service_adapter import TransferServiceAdapter
from src.remittances.infraestructure.web.security.ApiKeyValidation import validateRIA
from src.shared.adapters.backen_platform_adapter import BackendPlatformAdapter
from src.shared.tools.auth.access import api_key_ria, ip_whitelist

bp_ria = Blueprint('ria', __name__)

ria_endpoint = '/external/ria/transfer'


@bp_ria.route(ria_endpoint, methods=["POST"], strict_slashes=False)
@ip_whitelist
@api_key_ria
def ria():

    
    try:
        token = request.headers.get('token')
        data = request.get_json()

        customer_orm_service = CustomerORMService()
        customer_repository = CustomerRepositoryAdapter(customer_orm_service)

        transfer_application_service = TransferServiceApplication(
            ria_token=token,
            customer_repository=customer_repository
        )
        
        response = transfer_application_service.create_transfer(
            **data
        )
        
        
        return jsonify(response), response.get('statusCode', 500)
    
    except Exception as e:
        return jsonify({
            'statusCode': 500,
            'data': {
                'message': str(e)
            }
        }), 500