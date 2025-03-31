from general.argparser import MyParser
from general.start_type import StartType
from database import db_settings
from sql_db.sql_db_manager import SQL_DB_Manager
from json_db.json_db_manager import JsonDBManager
from console_manager import ConsoleToDo


def get_db_manager(db_type: str):
    """Создает и возвращает экземпляр менеджера БД"""
    match db_type:
        case "db_sql":
            return SQL_DB_Manager()
        case "db_json":
            return JsonDBManager()
        case _:
            raise ValueError("DB_TYPE должен быть либо db_sql, либо db_json")


def run_while_start(db):
    """Запуск в режиме бесконечного цикла"""
    console_manager = ConsoleToDo(db)
    console_manager.start_console()


def run_argparse_start(db):
    """Запуск в режиме argparse"""
    my_parser = MyParser(db)
    my_parser.add_arguments()


def main(db_settings):
    """Основная функция инициализации приложения"""
    db = get_db_manager(db_settings.DB_TYPE)

    match db_settings.START_TYPE:
        case "while_start":
            run_while_start(db)
        case "argparse_start":
            run_argparse_start(db)
        case _:
            raise ValueError(
                "Неизвестный тип запуска. Допустимо: argparse_start или while_start"
            )


if __name__ == "__main__":
    main(db_settings)
