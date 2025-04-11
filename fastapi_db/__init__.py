from fastapi import FastAPI
from AbstractDBManager import AbstractDBManager
from fastapi_db.fastapi_app import app, setup_db_manager

def create_fastapi_app(db_manager: AbstractDBManager) -> FastAPI:
    """Фабрика для создания FastAPI приложения с нужным менеджером БД"""
    setup_db_manager(db_manager)
    return app