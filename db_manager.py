from database import SessionLocal
from models import Task
from uuid import UUID
from TaskExceptions import *

class DB_Manager:
    def __init__(self):
        pass
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

    def mark_task(self, id: str) -> None:
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

    def delete_task(self, id: str) -> None:
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