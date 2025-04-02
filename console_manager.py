from uuid import UUID
from AbstractDBManager import AbstractDBManager

class ConsoleToDo:
    """
    Консольный менеджер для работы с базами данных
    """
    def __init__(self, db: AbstractDBManager) -> None:
        """
        Инициализатор консольного менеджера
        :param db: экземпляр менеджера базы данных
        :return: None
        """
        self.db_manager = db

    def start_console(self) -> None:
        """
        Метод выводящий меню работы с базами данных
        :return: None
        """
        while True:
            try:
                counts_ = 20
                print("_" * counts_)
                print("Выберите действие что делать дальше?")
                print("1. Вывести задачи")
                print("2. Добавить задачу")
                print("3. Редактировать задачу")
                print("4. Завершить задачу")
                print("5. Удалить задачу")
                print("6. Выйти")
                print("_" * counts_)
                select = input()
                match select:
                    case "1":
                        self.db_manager.print_tasks()
                    case "2":
                        name = input("Введите текст: ")
                        self.db_manager.add_task(name)
                        input()
                    case "3":
                        self.db_manager.print_tasks()
                        uuid = UUID(input("id: "))
                        name = input("text: ")
                        self.db_manager.edit_task(uuid, name)

                        input()
                    case "4":
                        self.db_manager.print_tasks()
                        uuid = UUID(input("id: "))
                        self.db_manager.mark_done(uuid)

                        input()
                    case "5":
                        self.db_manager.print_tasks()
                        uuid = UUID(input("id: "))
                        self.db_manager.delete_task(uuid)

                        input()
                    case "6":
                        return
                    case _:
                        print("Неправильный ввод")
                        return
            except Exception as e:
                    print(e)
