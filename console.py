from uuid import UUID
from database import SessionLocal
from models import Task
from TaskExceptions import *

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
            else:
                raise TaskExistingException(id=id)

    def mark_task(self, id) -> None:
        """
        Завершение таска
        :param id: id таска
        """
        with SessionLocal() as session:
            task = session.get(Task, UUID(id))
            if task:
                if task.is_active:
                    task.is_active = False
                    session.commit()
                else:
                    raise TaskAlreadyIsDone(id)
            else:
                raise TaskExistingException(id=id)


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
            else:
                raise TaskExistingException(id=id)


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
                    try:
                        self.edit_task(uuid, name)
                    except Exception as e:
                        print(e)
                    input()
                case "4":
                    self.print_tasks()
                    uuid = input("id: ")
                    try:
                        self.mark_task(uuid)
                    except Exception as e:
                        print(e)
                    input()
                case "5":
                    self.print_tasks()
                    uuid = input("id: ")
                    try:
                        self.delete_task(uuid)
                    except Exception as e:
                        print(e)
                    input()
                case "6":
                    return
                case _:
                    print("Неправильный ввод")
                    return
