from general.argparser import MyParser
from database import db_settings, DBSettings
from sql_db.sql_db_manager import SQLDBManager
from json_db.json_db_manager import JsonDBManager
from console_manager import ConsoleToDo
from fastapi_db import create_fastapi_app
import uvicorn

def get_db_manager(db_type: str) -> SQLDBManager | JsonDBManager:
    match db_type:
        case "db_sql":
            return SQLDBManager()
        case "db_json":
            return JsonDBManager()
        case _:
            raise ValueError("DB_TYPE должен быть либо db_sql, либо db_json")

def run_while_start(db: SQLDBManager | JsonDBManager) -> None:
    console_manager = ConsoleToDo(db)
    console_manager.start_console()

def run_argparse_start(db: SQLDBManager | JsonDBManager) -> None:
    my_parser = MyParser(db)
    my_parser.add_arguments()


def run_fastapi_start(db: SQLDBManager | JsonDBManager) -> None:
    """Запуск FastAPI с переданным менеджером БД"""
    # Устанавливаем менеджер БД для приложения
    from fastapi_db.fastapi_app import setup_db_manager
    setup_db_manager(db)

    # Запускаем через строку импорта для поддержки reload
    uvicorn.run(
        "fastapi_db.fastapi_app:app",
        port=1234,
        reload=True
    )

def main(db_settings: DBSettings) -> None:
    db = get_db_manager(db_settings.DB_TYPE)

    match db_settings.START_TYPE:
        case "while_start":
            run_while_start(db)
        case "argparse_start":
            run_argparse_start(db)
        case "fastapi":
            run_fastapi_start(db)
        case _:
            raise ValueError(
                "Неизвестный тип запуска. Допустимо: argparse_start, while_start или fastapi"
            )

if __name__ == "__main__":
    main(db_settings)