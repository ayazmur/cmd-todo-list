import os
import argparse
import json
from uuid import uuid4
class Task:
    def __init__(self, name):
        self.name = name
        self.active = True

class ConsoleToDo:
    def __init__(self):
        self.json_name = "db.json"
        self.data = self.__load_json(self.json_name)
        self.tasks = {}

    @staticmethod
    def __load_json(json_name: str) -> dict:
        """
        Загружает файл json
        :param json_name: полное имя файла json в корне
        :return: данные из json
        """
        if not os.path.exists(json_name) or os.path.getsize(json_name) == 0:
            with open(json_name, 'w', encoding="utf-8") as file:
                json.dump({}, file, ensure_ascii=False)
        with open(json_name, 'r', encoding="utf-8") as file:
            data = json.load(file)
            return data

    @staticmethod
    def save_json(json_name: str, data: dict):
        """
        Сохраняет json
        :param json_name: полное имя файла json в корне
        :param data: данные к сохранению в json
        """
        with open(json_name, 'w') as file:
            json.dump(data, file)

    def print_tasks(self):
        """
        Выводит таски в консоль
        """
        if not self.data:
            print("Нет данных")
        else:
            print("Список тасков:")
            for idf, task in self.data.items():
                print(f"{idf}. {task['name']} {task['active']}")

    def __generate_id(self) -> str:
        """
        Генерирует случайный uuid
        :return:
        str: случайный uuid
        """
        idf = str(uuid4())
        return idf
    def add_task(self):
        """
        Добавление таска
        """
        idf = self.__generate_id()
        print(f"Введите таск:")
        task = input()
        if not task:
            print("Пустой ввод")
            return
        task = Task(task)
        self.data[idf] = {'name': task.name, 'active': task.active}
        self.save_json(self.json_name, self.data)

    def edit_task(self):
        """
        Редактирование таска
        """
        idf = input("Введите id таска для редактирования: ")
        if idf in self.data.keys():
            print(f"Редактируемый таск: '{idf} {self.data[idf]}'")
            new_task = input(f"Введите новый таск:")
            if new_task not in self.data.values():
                self.data[idf]['name'] = new_task
                self.save_json(self.json_name, self.data)
            else:
                print(f"Таск '{new_task}' уже существует.")
        else:
            print(f"Таск '{idf}' не существует.")


    def mark_task(self):
        """
        Завершение таска
        """
        idf = input("Введите id таска для завершения: ")
        self.data[idf]['active'] = False
        print(f"Таск '{self.data[idf]}' завершен.")
        self.save_json(self.json_name, self.data)
    def delete_task(self):
        """
        Удаление таска
        """
        idf = input("Введите id таска для удаления: ")
        if idf in self.data.keys():
            print(f"Удаленный таск: '{self.data[idf]}'")
            del self.data[idf]
            self.save_json(self.json_name, self.data)
        else:
            print(f"Таск '{self.data[idf]}' не существует.")

    def delete_db(self):
        """
        Удаление базы данных
        """
        os.remove(self.json_name)

console_to_do = ConsoleToDo()
parser = argparse.ArgumentParser()
def __add_arguments():
    parser.add_argument('-pt', '--print_tasks', action='store_true', help="Print tasks to cli")
    parser.add_argument('-at', '--add_task', action='store_true', help="Add task")
    parser.add_argument('-et', '--edit_tasks', action='store_true', help="Edit task")
    parser.add_argument('-ddb', '--delete_data_base', action='store_true', help="Delete DB")
    parser.add_argument('-mt', '--mark_task', action='store_true', help="Mark task")
    parser.add_argument('-dt', '--delete_task', action='store_true', help="Delete task")
    args = parser.parse_args()
    if args.print_tasks:
        console_to_do.print_tasks()
    elif args.add_task:
        console_to_do.add_task()
    elif args.edit_tasks:
        console_to_do.edit_task()
    elif args.delete_data_base:
        console_to_do.delete_db()
    elif args.mark_task:
        console_to_do.mark_task()
    elif args.delete_task:
        console_to_do.delete_task()
__add_arguments()


