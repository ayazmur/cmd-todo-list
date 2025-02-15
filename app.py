import os
import argparse
import json
from random import randint
parser = argparse.ArgumentParser()
class ConsoleToDo:
    def __init__(self):
        self.json_name = "db.json"
        self.data = self.load_json(self.json_name)
        self.tasks = {}

    @staticmethod
    def load_json(json_name):
        """
        Загружает файл json
        :param json_name: полное имя файла json в корне
        :return: данные из json
        """
        if not os.path.exists(json_name):
            with open(json_name, 'w') as file:
                json.dump({}, file)
        with open(json_name, 'r') as file:
            data = json.load(file)
            return data

    @staticmethod
    def save_json(json_name, data):
        """
        Сохраняет json
        :param json_name: полное имя файла json в корне
        :param data: данные к сохранию в json
        """
        with open(json_name, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def print_tasks(data):
        """
        Выводит таски в консоль
        :param data: данные из json
        """
        if not data:
            print("Нет данных")
        else:
            print("Список тасков:")
            for idf, task in data.items():
                print(f"{idf}. {task}")

    def generate_id(self):
        """
        Генерирует случайное число
        :return:
        int: случайное число (0-999999)
        """
        idf = randint(0,999999)
        if idf not in self.data.keys():
            return idf
        else:
            self.generate_id()

    def add_task(self):
        """
        Добавление таска
        """
        idf = self.generate_id()
        print(f"Введите таска:")
        task = input()
        if not task:
            print("Пустой ввод")
        if task not in self.data.values():
            self.data[idf] = task
        else:
            print(f"Таск '{task}' уже существует.")
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
                self.data[idf] = new_task
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
        self.data[idf] = f"{self.data[idf]}(Готово)"
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

    def return_tasks(self):
        """
        Вывод таска в консоль
        """
        self.print_tasks(self.data)
    def delete_db(self):
        """
        Удаление базы данных
        """
        os.remove(self.json_name)

console_to_do = ConsoleToDo()

def add_arguments():
    parser.add_argument('-pt', '--print_tasks', action='store_true', help="Print tasks to cli")
    parser.add_argument('-at', '--add_task', action='store_true', help="Add task")
    parser.add_argument('-et', '--edit_tasks', action='store_true', help="Edit task")
    parser.add_argument('-ddb', '--delete_data_base', action='store_true', help="Delete DB")
    parser.add_argument('-mt', '--mark_task', action='store_true', help="Mark task")
    parser.add_argument('-dt', '--delete_task', action='store_true', help="Delete task")
    args = parser.parse_args()
    if args.print_tasks:
        console_to_do.return_tasks()
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

add_arguments()


