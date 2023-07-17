# src\name_service\infraestructure\web\entrypoints\sample_blueprint.py

from flask import Blueprint, request, Response
from src.name_service.application.services.sample_service import SampleCreateEntityService
from src.shared.tools.auth.access import login_required

bp_sample = Blueprint('sample', __name__)

sample_endpoint = '/sample'


@bp_sample.route(sample_endpoint, methods=["POST"], strict_slashes=False)
# @login_required(user_info=False)
def sample():

    sample_data = request.json
    try:
        service = SampleCreateEntityService(sample_data.get('sample_property'))
        service.execute()
    except Exception as e:
        return Response(f"Error processing request: {str(e)}", 500)
