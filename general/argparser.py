import argparse
from AbstractDBManager import AbstractDBManager

class MyParser(argparse.ArgumentParser):
    """
    Класс парсера для работы с базой данных через аргументы консоли
    """
    def __init__(self, db_manager:AbstractDBManager) -> None:
        """
        Инициализатор парсера для ввода в консоль
        :param db_manager: экземпляр менеджера базы данных
        :return: None
        """
        super().__init__()
        self.db_manager = db_manager

    def add_arguments(self) -> None:
        """
        Метод добавляющий аргументы в парсер
        :return: None
        """
        self.add_argument(
            "-pt", "--print_tasks", action="store_true", help="Print tasks to cli"
        )
        self.add_argument("-at", "--add_task", nargs=1, metavar="TEXT", help="Add task")
        self.add_argument("-md", "--mark_done", nargs=1, metavar="ID", help="Mark task")
        self.add_argument(
            "-et",
            "--edit_task",
            nargs=2,  # Ожидаем 2 аргумента: id и text
            metavar=("ID", "TEXT"),  # Для красивого отображения в help
            help="Edit task. Usage: -et ID TEXT",
        )
        self.add_argument(
            "-dt", "--delete_task", nargs=1, metavar="ID", help="Delete task"
        )

        args = self.parse_args()
        if args.print_tasks:
            self.db_manager.print_tasks()
        elif args.add_task:
            text = args.add_task
            self.db_manager.add_task(text[0])
        elif args.edit_task:
            uid, new_text = args.edit_task
            self.db_manager.edit_task(uid, new_text)
        elif args.mark_done:
            uid = args.mark_done
            self.db_manager.mark_done(uid[0])
        elif args.delete_task:
            uid = args.delete_task
            self.db_manager.delete_task(uid[0])
