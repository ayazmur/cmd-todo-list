from uuid import UUID
import os
from database import SessionLocal
from models import Task
class ConsoleToDo:
    def __init__(self):
        self.json_name = "db.json"
        self.tasks = {}

    def print_tasks(self):
        """
        Выводит таски в консоль
        """
        with SessionLocal() as session:
            tasks = session.query(Task).all()
            for task in tasks:
                print(f"id: {task.id} name: {task.name} active: {task.active}")




    def add_task(self, text):
        """
        Добавление таска
        """
        with SessionLocal() as session:
            task = Task(name = text)
            session.add(task)
            session.commit()

    def edit_task(self, id, text):
        """
        Редактирование таска
        """
        with SessionLocal() as session:
            task = session.get(Task, UUID(id))
            if task:
                task.name = text
                session.commit()
            else:
                print(f"Таск не существует.")

    def mark_task(self, id):
        """
        Завершение таска
        """
        with SessionLocal() as session:
            task = session.get(Task, UUID(id))
            if task:
                task.active = False
                session.commit()
            else:
                print(f"Таск не существует.")

    def delete_task(self, id):
        """
        Удаление таска
        """
        with SessionLocal() as session:
            task = session.get(Task, UUID(id))
            if task:
                session.delete(task)
                session.commit()
            else:
                print(f"Таск не существует.")


    def start_console(self):
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
