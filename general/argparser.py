import argparse


class MyParser(argparse.ArgumentParser):
    def __init__(self, console_to_do):
        """
        :param console_to_do: экземпляр класса консольного ввода
        """
        super().__init__()
        self.console_to_do = console_to_do

    def add_arguments(self) -> None:
        self.add_argument(
            "-pt", "--print_tasks", action="store_true", help="Print tasks to cli"
        )
        self.add_argument("-at", "--add_task", nargs=1, metavar="TEXT", help="Add task")
        self.add_argument("-md", "--mark_done", nargs=1, metavar="ID", help="Mark task")
        self.add_argument(
            "-et",
            "--edit_task",
            nargs=2,  # Ожидаем 2 аргумента: id и text
            metavar=("ID", "TEXT"),  # Для красивого отображения в help
            help="Edit task. Usage: -et ID TEXT",
        )
        self.add_argument(
            "-dt", "--delete_task", nargs=1, metavar="ID", help="Delete task"
        )

        args = self.parse_args()
        if args.print_tasks:
            self.console_to_do.print_tasks()
        elif args.add_task:
            text = args.add_task
            self.console_to_do.add_task(text[0])
        elif args.edit_task:
            uid, new_text = args.edit_task
            self.console_to_do.edit_task(uid, new_text)
        elif args.mark_done:
            uid = args.mark_done
            self.console_to_do.mark_done(uid[0])
        elif args.delete_task:
            uid = args.delete_task
            self.console_to_do.delete_task(uid[0])
