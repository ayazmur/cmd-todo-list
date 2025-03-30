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
        self.add_argument("-at", "--add_task", action="store_true", help="Add task")
        self.add_argument("-et", "--edit_tasks", action="store_true", help="Edit task")
        self.add_argument("-mt", "--mark_task", action="store_true", help="Mark task")
        self.add_argument(
            "-dt", "--delete_task", action="store_true", help="Delete task"
        )
        self.add_argument(
            "-sc", "--start_console", action="store_true", help="Start console"
        )

        args = self.parse_args()
        if args.print_tasks:
            self.console_to_do.print_tasks()
        elif args.add_task:
            self.console_to_do.add_task()
        elif args.edit_tasks:
            self.console_to_do.edit_task()
        elif args.mark_task:
            self.console_to_do.mark_task()
        elif args.delete_task:
            self.console_to_do.delete_task()
        elif args.start_console:
            self.console_to_do.start_console()
