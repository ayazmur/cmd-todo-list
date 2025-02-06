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
        Load json file
        :param json_name: full name of json file on project root
        :return: data from json file
        """
        if not os.path.exists(json_name):
            with open(json_name, 'w') as file:
                json.dump({}, file)
        with open(json_name, 'r') as file:
            data = json.load(file)
            return data

    @staticmethod
    def save_json(json_name, data):
        with open(json_name, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def print_tasks(data):
        """
        Print tasks to console
        :param data: dota from json file
        :return: prints tasks to console
        """
        if not data:
            print("No data")
        else:
            print("Tasks list:")
            for idf, task in data.items():
                print(f"{idf}. {task}")

    def generate_id(self):
        """
        Generate random id not existing in db
        :return:
        int: random id (0-999999)
        """
        idf = randint(0,999999)
        if idf not in self.data.keys():
            return idf
        else:
            self.generate_id()

    def add_task(self):
        """
        Add task to db
        """
        idf = self.generate_id()
        print(f"Enter task:")
        task = input()
        if not task:
            print("No task")
        if task not in self.data.values():
            self.data[idf] = task
        else:
            print(f"Task '{task}' already exists.")
        self.save_json(self.json_name, self.data)

    def edit_task(self):
        """
        Edit task in db
        :return:
        """
        idf = input("Enter id of task to edit: ")
        if idf in self.data.keys():
            print(f"Edit task: '{idf} {self.data[idf]}' to change")
            new_task = input(f"Enter new task:")
            if new_task not in self.data.values():
                self.data[idf] = new_task
                self.save_json(self.json_name, self.data)
            else:
                print(f"Task '{new_task}' already exists.")
        else:
            print(f"Task '{idf}' does not exist.")

    #FIXME
    @staticmethod
    def strike(text):
        """
        Definition that must strike text
        :param text: string to strike
        :return: strike text
        """
        result = ""
        for char in text:
            result += result + char + '\u0336'
        return result

    def mark_task(self):
        """
        Mark task in db
        :return:
        """
        idf = input("Enter id of task to mark done: ")
        self.data[idf] = f"{self.data[idf]}(done)"
        print(f"Task '{self.data[idf]}' has been mark as done.")
        self.save_json(self.json_name, self.data)
    def delete_task(self):
        idf = input("Enter id of task to delete: ")
        if idf in self.data.keys():
            print(f"Deleted task: '{self.data[idf]}'")
            del self.data[idf]
            self.save_json(self.json_name, self.data)
        else:
            print(f"Task '{self.data[idf]}' does not exist.")

    def return_tasks(self):
        self.print_tasks(self.data)
    def delete_db(self):
        os.remove(self.json_name)

console_to_do = ConsoleToDo()
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

