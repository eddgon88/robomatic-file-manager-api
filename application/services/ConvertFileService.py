import pandas as pd
import os

class ConvertFileService:
    @staticmethod
    def convert_file(fileName: str, fileExtention: str, executionId: str):
        orinfileDir = os.environ['EVIDENCE_FILE_DIR'] + executionId + '/' +  fileName
        fileNameWde = fileName[0:fileName.find(".")]
        newFileDir = os.environ['EVIDENCE_FILE_DIR'] + executionId + '/' +  fileNameWde + '.' + fileExtention
        
        df = pd.read_csv(orinfileDir, sep=",")
        writer = pd.ExcelWriter(newFileDir, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.close()
        
        return True