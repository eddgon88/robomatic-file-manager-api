# application/order_api/routes.py
from flask import jsonify, request, make_response
from . import file_manager_blueprint
from .api.services.ConvertFileService import ConvertFileService

@file_manager_blueprint.route('/file-manager-api/vi/convert', methods=['POST'])
def checkout():
    content = request.get_json()
    print(content)
    fileName = content['file_name']
    fileExtention = content['file_extention']
    executionId = content['execution_id']
    file = ConvertFileService.convert_file(fileName, fileExtention, executionId)
    print(file)
    return "True"
