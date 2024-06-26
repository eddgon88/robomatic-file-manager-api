# run.py
from application.main import create_app
import uvicorn

app = create_app()

if __name__ == "__main__":
    uvicorn.run("run:app", host="0.0.0.0", port=5000, log_level="info")
