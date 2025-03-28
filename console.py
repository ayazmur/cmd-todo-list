from uuid import UUID
from database import SessionLocal
from models import Task


class ConsoleToDo:
    def __init__(self):
        self.tasks = {}

    def print_tasks(self) -> None:
        """
        Выводит таски в консоль
        """
        with SessionLocal() as session:
            tasks = session.query(Task).all()
            for task in tasks:
                print(f"id: {task.id} name: {task.task_text} active: {task.is_active}")

    def add_task(self, text: str) -> None:
        """
        Добавление таска
        :param text: текст таска
        """
        with SessionLocal() as session:
            task = Task(task_text=text)
            session.add(task)
            session.commit()
            session.refresh()

    def edit_task(self, id: str, text: str) -> None:
        """
        Редактирование таска
        :param id: id таска
        :param text: новый текст таска
        """
        with SessionLocal() as session:
            task = session.get(Task, UUID(id))
            if task:
                task.task_text = text
                session.commit()
                session.refresh()
            else:
                print(f"Таск с id {id} не существует.")

    def mark_task(self, id) -> None:
        """
        Завершение таска
        :param id: id таска
        """
        with SessionLocal() as session:
            task = session.get(Task, UUID(id))
            if task:
                task.is_active = False
                session.commit()
                session.refresh()
            else:
                print(f"Таск не существует.")

    def delete_task(self, id) -> None:
        """
        Удаление таска
        :param id: id таска
        """
        with SessionLocal() as session:
            task = session.get(Task, UUID(id))
            if task:
                session.delete(task)
                session.commit()
                session.refresh()
            else:
                print(f"Таск не существует.")

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
                    self.print_tasks()
                case "2":
                    name = input("Введите текст: ")
                    self.add_task(name)
                    input()
                case "3":
                    self.print_tasks()
                    uuid = input("id: ")
                    name = input("text: ")
                    self.edit_task(uuid, name)
                    input()
                case "4":
                    self.print_tasks()
                    uuid = input("id: ")
                    self.mark_task(uuid)
                    input()
                case "5":
                    self.print_tasks()
                    uuid = input("id: ")
                    self.delete_task(uuid)
                    input()
                case "6":
                    return
                case _:
                    print("Неправильный ввод")
                    return
