from general.argparser import MyParser
from general.start_type import StartType
from database import db_settings
from sql_db.sql_db_manager import SQL_DB_Manager
from json_db.json_db_manager import JsonDBManager
from console_manager import ConsoleToDo

start_type = StartType.WHILE_START
if __name__ == "__main__":

    if start_type == StartType.WHILE_START:
        match db_settings.DB_TYPE:
            case "db_sql":
                db = SQL_DB_Manager()
            case "db_json":
                db = JsonDBManager()
            case _:
                raise ValueError("DB_TYPE должен быть либо sql_db или json")
        console_manager = ConsoleToDo(db)
        console_manager.start_console()

    elif start_type == StartType.ARGPARSE_START:
        pass
        # my_parser = MyParser(console_to_do)
        # my_parser.add_arguments()
    else:
        raise ValueError("Неизвестный тип запуска программы")
