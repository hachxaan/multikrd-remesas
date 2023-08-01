# src\remittances\infraestructure\web\entrypoints\ria_blueprint.py

from flask import Blueprint, request, Response
from src.remittances.infraestructure.exceptions.AccessDeniedException import AccessDeniedException
from src.remittances.infraestructure.web.security.ApiKeyValidation import validateRIA
from src.shared.tools.auth.access import api_key_ria, ip_whitelist

bp_ria = Blueprint('ria', __name__)

ria_endpoint = '/external/ria/transfer'


@bp_ria.route(ria_endpoint, methods=["POST"], strict_slashes=False)
@ip_whitelist
@api_key_ria
def ria():

    
    try:
        if not validateRIA(
            x_api_key=request.headers.get('x-api-key'),
            xRealIp=request.remote_addr,
        ):
            raise AccessDeniedException('Access denied')

        
    

    except Exception as e:
        return Response(f"Error processing request: {str(e)}", 500)
