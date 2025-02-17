from console import ConsoleToDo
from argparser import MyParser

if __name__ == "__main__":
    console_to_do = ConsoleToDo()
    my_parser = MyParser(console_to_do)
    console_to_do.start_console()
