import json
from uuid import uuid4
from task import Task
import os


class ConsoleToDo:
    def __init__(self):
        self.json_name = "db.json"
        self.data = self._load_json()
        self.tasks = {}

    def _load_json(self) -> dict:
        """
        Загружает файл json
        :return: данные из json
        """
        if not os.path.exists(self.json_name) or os.path.getsize(self.json_name) == 0:
            with open(self.json_name, "w", encoding="utf-8") as file:
                json.dump({}, file, ensure_ascii=False)

        with open(self.json_name, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data

    def save_json(self):
        """
        Сохраняет json
        """
        with open(self.json_name, "w") as file:
            json.dump(self.data, file)

    def print_tasks(self):
        """
        Выводит таски в консоль
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
        idf = uuid4()
        return idf

    def add_task(self):
        """
        Добавление таска
        """
        idf = str(self._generate_id())
        print(f"Введите таск:")
        task = input()
        if not task:
            print("Пустой ввод")
            return
        task = Task(task)
        self.data[idf] = {"name": task.name, "active": task.active}
        self.save_json()

    def edit_task(self):
        """
        Редактирование таска
        """
        idf = input("Введите id таска для редактирования: ")
        if idf in self.data.keys():
            print(f"Редактируемый таск: '{idf} {self.data[idf]}'")
            new_task = input(f"Введите новый таск:")
            self.data[idf]["name"] = new_task
            self.save_json()
        else:
            print(f"Таск '{idf}' не существует.")

    def mark_task(self):
        """
        Завершение таска
        """
        idf = input("Введите id таска для завершения: ")
        self.data[idf]["active"] = False
        print(f"Таск '{self.data[idf]}' завершен.")
        self.save_json()

    def delete_task(self):
        """
        Удаление таска
        """
        idf = input("Введите id таска для удаления: ")
        if idf in self.data.keys():
            print(f"Удаленный таск: '{self.data[idf]}'")
            del self.data[idf]
            self.save_json()
        else:
            print(f"Таск '{self.data[idf]}' не существует.")

    def delete_db(self):
        """
        Удаление базы данных
        """
        os.remove(self.json_name)
