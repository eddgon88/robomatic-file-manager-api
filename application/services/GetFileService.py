import os
import base64
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO,
                    format='(%(threadName)-10s) %(message)s',)

class GetFileService:
    @staticmethod
    def get_list_test_execution(executionId: str):
        print("buscando evidencias")
        EVIDENCE_FILE_DIR = os.getenv("EVIDENCE_FILE_DIR")
        dir_path = EVIDENCE_FILE_DIR + executionId
        #dir_path = settings.get('EVIDENCE_FILE_DIR')
        print(dir_path)
        res = []
        for file_path in os.listdir(dir_path):
            # check if current file_path is a file
            if os.path.isfile(os.path.join(dir_path, file_path)):
                # add filename to list
                with open(os.path.join(dir_path, file_path), "r") as f_in:
                    data = f_in.read()
                data_bytes = data.encode('utf8')
                base64_bytes = base64.b64encode(data_bytes)
                base64_data = base64_bytes.decode('utf8')
                res.append({
                    'file_name': file_path,
                    'file_content': base64_data,
                })
        return res
    
    @staticmethod
    def get_file(execution_id: str, filename: str):
        EVIDENCE_FILE_DIR = os.getenv("EVIDENCE_FILE_DIR")
        logging.info("EVIDENCE_FILE_DIR - %s", EVIDENCE_FILE_DIR)
        logging.info("execution_id - %s", execution_id)
        logging.info("filename - %s", filename)
        dir_path = EVIDENCE_FILE_DIR + execution_id + "/" + filename
        with open(dir_path, "rb") as f:
            return f.read()