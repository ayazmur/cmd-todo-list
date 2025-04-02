from general.argparser import MyParser
from database import db_settings, DBSettings
from sql_db.sql_db_manager import SQLDBManager
from json_db.json_db_manager import JsonDBManager
from console_manager import ConsoleToDo


def get_db_manager(db_type: str) -> SQLDBManager | JsonDBManager:
    """
    Создает и возвращает экземпляр менеджера БД
    :param db_type: флаг типа базы данных
    :return: SQLDBManager | JsonDBManager
    """
    match db_type:
        case "db_sql":
            return SQLDBManager()
        case "db_json":
            return JsonDBManager()
        case _:
            raise ValueError("DB_TYPE должен быть либо db_sql, либо db_json")


def run_while_start(db: SQLDBManager | JsonDBManager) -> None:
    """
    Запуск в режиме бесконечного цикла
    :param db: экземпляр базы данных
    :return: None
    """
    console_manager = ConsoleToDo(db)
    console_manager.start_console()


def run_argparse_start(db: SQLDBManager | JsonDBManager) -> None:
    """
    Запуск в режиме argparse
    :param db: экземпляр базы данных
    :return: None
    """
    my_parser = MyParser(db)
    my_parser.add_arguments()


def main(db_settings: DBSettings) -> None:
    """
    Основная функция инициализации приложения
    :param db_settings: экземпляр настроек базы данных
    :return: None
    """
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
