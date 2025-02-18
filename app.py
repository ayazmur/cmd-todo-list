from console import ConsoleToDo
from argparser import MyParser
from start_type import StartType
start_type = StartType.ARGPARSE_START
if __name__ == "__main__":
    console_to_do = ConsoleToDo()
    my_parser = MyParser(console_to_do)
    my_parser.add_arguments()
    if start_type == StartType.WHILE_START:
        console_to_do.start_console()


