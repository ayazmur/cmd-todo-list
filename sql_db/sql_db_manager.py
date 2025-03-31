from database import SessionLocal
from sql_db.models import Task
from uuid import UUID
from general.TaskExceptions import *


class SQL_DB_Manager:
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
            session.refresh(task)

    def edit_task(self, id: UUID, text: str) -> None:
        """
        Редактирование таска
        :param id: id таска
        :param text: новый текст таска
        """
        with SessionLocal() as session:
            task = session.get(Task, id)
            if task:
                task.task_text = text
                session.commit()
                session.refresh(task)
            else:
                raise TaskExistingException(id=id)

    def mark_done(self, id: UUID) -> None:
        """
        Завершение таска
        :param id: id таска
        """
        with SessionLocal() as session:
            task = session.get(Task, id)
            if task:
                if task.is_active:
                    task.is_active = False
                    session.commit()
                    session.refresh(task)
                else:
                    raise TaskCompletedException(id)
            else:
                raise TaskExistingException(id=id)

    def delete_task(self, id: UUID) -> None:
        """
        Удаление таска
        :param id: id таска
        """
        with SessionLocal() as session:
            task = session.get(Task, id)
            if task:
                session.delete(task)
                session.commit()
            else:
                raise TaskExistingException(id=id)
