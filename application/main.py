# application/__init__.py
from fastapi import FastAPI
from .routers import apirouter
from . import config

app_configs = {"title": "file-manager-api",
               "EVIDENCE_FILE_DIR": config.EVIDENCE_FILE_DIR}

def create_app():
    app = FastAPI(**app_configs)
    app.include_router(apirouter.router)
    return app
        
