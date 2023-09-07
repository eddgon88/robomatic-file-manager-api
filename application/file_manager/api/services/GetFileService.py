import os
import base64

class GetFileService:
    @staticmethod
    def get_list_test_execution(executionId: str):
        dir_path = os.environ['EVIDENCE_FILE_DIR'] + executionId
        res = []
        for file_path in os.listdir(dir_path):
            # check if current file_path is a file
            if os.path.isfile(os.path.join(dir_path, file_path)):
                # add filename to list
                with open(os.path.join(dir_path, file_path), "r") as f_in:
                    data = f_in.read()
                data_bytes = data.encode('ascii')
                base64_bytes = base64.b64encode(data_bytes)
                base64_data = base64_bytes.decode('ascii')
                res.append({
                    'file_name': file_path,
                    'file_content': base64_data,
                })
        return res