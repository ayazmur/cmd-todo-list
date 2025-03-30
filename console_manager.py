from db_manager import DB_Manager
from uuid import UUID

class ConsoleToDo:
    def __init__(self):
        self.db_manager = DB_Manager()

    def start_console(self) -> None:
        while True:
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
                    try:
                        self.db_manager.edit_task(uuid, name)
                    except Exception as e:
                        print(e)
                    input()
                case "4":
                    self.db_manager.print_tasks()
                    uuid = UUID(input("id: "))
                    try:
                        self.db_manager.mark_done(uuid)
                    except Exception as e:
                        print(e)
                    input()
                case "5":
                    self.db_manager.print_tasks()
                    uuid = UUID(input("id: "))
                    try:
                        self.db_manager.delete_task(uuid)
                    except Exception as e:
                        print(e)
                    input()
                case "6":
                    return
                case _:
                    print("Неправильный ввод")
                    return
