from AbstractDBManager import AbstractDBManager
import os
import json
from uuid import uuid4
from json_db.task import Task
from general.TaskExceptions import *
from uuid import UUID

class JsonDBManager(AbstractDBManager):
    def __init__(self) -> None:
        self.json_name = "json_db/db.json"
        self.data = self._load_json()
        self.tasks = {}

    def _load_json(self) -> dict:
        """
        Загружает файл json
        :return: данные из json
        """
        if not os.path.exists(self.json_name):
            with open(self.json_name, "w", encoding="utf-8") as file:
                json.dump({}, file, ensure_ascii=False)

        with open(self.json_name, "r+", encoding="utf-8") as file:
            content = file.read()
            file.seek(0)
            if len(content) == 0:
                file.write("{}")
                file.truncate()
            data = json.load(file)
            return data

    def _save_json(self) -> None:
        """
        Сохраняет json
        :return: None
        """
        with open(self.json_name, "w") as file:
            json.dump(self.data, file)

    def print_tasks(self) -> None:
        """
        Вывод всех тасков в консоль
        :return: None
        """
        if not self.data:
            print("Нет данных")
        else:
            print("Список тасков:")
            for idf, task in self.data.items():
                print(f"{idf}  {task['name']} {task['active']}")

    def _generate_id(self) -> uuid4:
        """
        Генерирует случайный uuid
        :return: случайный uuid
        """
        idf = str(uuid4())
        return idf

    def add_task(self, text: str) -> None:
        """
        Создание нового таска
        :param text: Текст нового таска
        :return: None
        """
        idf = str(self._generate_id())
        task = Task(text)
        self.data[idf] = {"name": task.name, "active": task.active}
        self._save_json()

    def edit_task(self, uid: UUID, text: str) -> None:
        """
        Редактирование таска
        :param uid: uid редактируемого таска
        :param text: Новый текст редактируемого таска
        :return: None
        """
        uid = str(uid)
        if uid in self.data.keys():
            print(f"Редактируемый таск: '{uid} {self.data[uid]}'")
            self.data[uid]["name"] = text
            self._save_json()
        else:
            raise TaskExistingException(id = uid)

    def mark_done(self, uid: str) -> None:
        """
        Завершение задачи
        :param uid: uid завершаемого таска
        :return: None
        """
        uid = str(uid)
        if uid in self.data.keys():
            self.data[uid]["active"] = False
            print(f"Таск '{self.data[uid]}' завершен.")
            self._save_json()
        else:
            raise TaskExistingException(id = uid)

    def delete_task(self, uid: str) -> None:
        """
        Удаление таска
        :param uid: uid удаляемого таска
        :return: None
        """
        uid = str(uid)
        if uid in self.data.keys():
            print(f"Удаленный таск: '{self.data[uid]}'")
            del self.data[uid]
            self._save_json()
        else:
            raise TaskExistingException(id = uid)
