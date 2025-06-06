import os
import base64
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='(%(threadName)-10s) %(message)s',
)

class GetFileService:
    @staticmethod
    def get_list_test_execution(executionId: str):
        """
        Obtiene una lista de archivos .txt y .csv en el directorio de evidencias para un executionId.
        Codifica el contenido de los archivos en Base64.

        Args:
            executionId (str): ID de la ejecución.

        Returns:
            List[dict]: Lista de diccionarios con nombre y contenido Base64 de los archivos.
        """
        try:
            EVIDENCE_FILE_DIR = os.getenv("EVIDENCE_FILE_DIR")
            if not EVIDENCE_FILE_DIR:
                logging.error("EVIDENCE_FILE_DIR no está configurado en las variables de entorno")
                raise ValueError("EVIDENCE_FILE_DIR no está configurado")

            dir_path = os.path.join(EVIDENCE_FILE_DIR, executionId)
            logging.info(f"Buscando evidencias en: {dir_path}")

            if not os.path.exists(dir_path):
                logging.error(f"El directorio no existe: {dir_path}")
                raise FileNotFoundError(f"El directorio no existe: {dir_path}")

            res = []
            # Extensiones permitidas
            allowed_extensions = {'.txt', '.csv'}
            
            for file_path in os.listdir(dir_path):
                full_path = os.path.join(dir_path, file_path)
                # Verificar si es un archivo y tiene una extensión permitida
                if os.path.isfile(full_path) and os.path.splitext(file_path)[1].lower() in allowed_extensions:
                    try:
                        # Leer como texto con UTF-8, manejando errores de decodificación
                        with open(full_path, "r", encoding='utf-8', errors='replace') as f_in:
                            data = f_in.read()
                        data_bytes = data.encode('utf-8')
                        
                        # Codificar en Base64
                        base64_bytes = base64.b64encode(data_bytes)
                        base64_data = base64_bytes.decode('utf-8')
                        
                        res.append({
                            'file_name': file_path,
                            'file_content': base64_data,
                        })
                        logging.info(f"Archivo procesado: {file_path}")
                    except Exception as e:
                        logging.error(f"Error al procesar archivo {file_path}: {str(e)}")
                        continue  # Continuar con el siguiente archivo

            logging.info(f"Se encontraron {len(res)} archivos (.txt o .csv) para executionId: {executionId}")
            return res

        except Exception as e:
            logging.error(f"Error al obtener lista de evidencias para executionId {executionId}: {str(e)}")
            raise

    @staticmethod
    def get_file(execution_id: str, filename: str):
        """
        Lee un archivo específico y devuelve su contenido en bytes.

        Args:
            execution_id (str): ID de la ejecución.
            filename (str): Nombre del archivo.

        Returns:
            bytes: Contenido del archivo.
        """
        try:
            EVIDENCE_FILE_DIR = os.getenv("EVIDENCE_FILE_DIR")
            if not EVIDENCE_FILE_DIR:
                logging.error("EVIDENCE_FILE_DIR no está configurado en las variables de entorno")
                raise ValueError("EVIDENCE_FILE_DIR no está configurado")

            dir_path = os.path.join(EVIDENCE_FILE_DIR, execution_id, filename)
            logging.info(f"Leyendo archivo: {dir_path}")

            if not os.path.exists(dir_path):
                logging.error(f"El archivo no existe: {dir_path}")
                raise FileNotFoundError(f"El archivo no existe: {dir_path}")

            with open(dir_path, "rb") as f:
                return f.read()

        except Exception as e:
            logging.error(f"Error al leer archivo {filename} para executionId {execution_id}: {str(e)}")
            raise