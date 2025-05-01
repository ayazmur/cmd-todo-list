import uvicorn

from general.argparser import MyParser
from src.config.database import db_settings, DBSettings
from src.interfaces.AbstractDBManager import AbstractDBManager
from src.services.console_manager import ConsoleToDo
from src.services.json_db_manager import JsonDBManager
from src.services.sql_db_manager import SQLDBManager
from web.web_app.web_app import setup_db_manager


def get_db_manager(db_type: str) -> SQLDBManager | JsonDBManager:
    """
    Получение экземпляра менеджера базы данных
    :param db_type: str
    :return: SQLDBManager | JsonDBManager
    """
    match db_type:
        case "db_sql":
            return SQLDBManager()
        case "db_json":
            return JsonDBManager()
        case _:
            raise ValueError("DB_TYPE должен быть либо db_sql, либо db_json")


def run_while_start(db: AbstractDBManager) -> None:
    """
    Запуск через консоль с переданным менеджером БД
    :param db: экземпляр менеджера базы данных
    :return: None
    """
    console_manager = ConsoleToDo(db)
    console_manager.start_console()


def run_argparse_start(db: AbstractDBManager) -> None:
    """
    Запуск через argparse с переданным менеджером БД
    :param db: экземпляр менеджера базы данных
    :return: None
    """
    my_parser = MyParser(db)
    my_parser.add_arguments()


def run_fastapi_start(db: AbstractDBManager) -> None:
    """
    Запуск fastapi с переданным менеджером БД
    :param db: экземпляр менеджера базы данных
    :return: None
    """

    setup_db_manager(db)

    # Запускаем через строку импорта для поддержки reload
    uvicorn.run("web.web_app.web_app:app", port=1234, reload=True)


def main(db_settings: DBSettings) -> None:
    """
    Основной запуск программы
    :param db_settings: экземпляр менеджера базы данных
    :return: None
    """
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
