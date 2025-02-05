import os
import sys
import argparse
import json
from random import sample, randint
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
    def save_json(self, json_name, data):
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

    def add_task(self):
        """
        Add task to db
        """
        idf = self.generate_id()
        print(f"Enter task:")
        task = input()
        self.data[idf] = task
        self.save_json(self.json_name, self.data)
    def red_task(self):
        pass
    def delete_task(self):
        pass
    def return_tasks(self):
        self.print_tasks(self.data)

console_to_do = ConsoleToDo()
parser.add_argument('-sc', '--start_cli',action='store_true', help="Запустить cli")
parser.add_argument('-pr','--print_hello', action='store_true', help="Hello world!")
parser.add_argument('-pt', '--print_tasks', action='store_true', help="Print tasks to cli")
parser.add_argument('-at', '--add_task', action='store_true', help="Add task")
args = parser.parse_args()
if args.print_tasks:
    console_to_do.return_tasks()
elif args.add_task:
    console_to_do.add_task()

