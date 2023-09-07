# application/order_api/routes.py
from flask import jsonify, request, make_response
from . import file_manager_blueprint
from .api.services.ConvertFileService import ConvertFileService
from .api.services.GetFileService import GetFileService

#@file_manager_blueprint.post('/file-manager-api/vi/convert')
#def checkout():
#    content = request.get_json()
#    print(content)
#    fileName = content['file_name']
#    fileExtention = content['file_extention']
#    executionId = content['execution_id']
#    file = ConvertFileService.convert_file(fileName, fileExtention, executionId)
#    print(file)
#    return "True"

@file_manager_blueprint.get('/file-manager-api/vi/file/<test_execution>')
def checkout(test_execution):
    fileArray = GetFileService.get_list_test_execution(test_execution)
    print(fileArray)
    print(fileArray.__class__)
    return jsonify(fileArray)
