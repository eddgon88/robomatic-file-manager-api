from fastapi import APIRouter
from pydantic import BaseModel
from ..services.ConvertFileService import ConvertFileService
from ..services.GetFileService import GetFileService


class RequestParams(BaseModel):
    file_name: str
    file_extention: str
    execution_id: str

router = APIRouter(prefix="/file-manager-api/vi")

@router.post("/convert", status_code=200)
def convert_file(params: RequestParams):
    file = ConvertFileService.convert_file(params.file_name, params.file_extention, params.execution_id)
    print(file)
    return "True"

@router.get("/file/{test_execution}")
def get_files(test_execution):
    fileArray = GetFileService.get_list_test_execution(test_execution)
    return fileArray