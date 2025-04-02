class TaskExistingException(Exception):
    """
    Пользовательское исключение вызываемое при отсутствии таска
    """
    def __init__(self, id=None, task_text=None) -> None:
        """
        Инициализатор исключения
        :param id: уникальный идентификатор таска
        :param task_text: текст таска
        :return: None
        """
        self.error_message = ""
        if id is not None:
            self.task_id = id
            self.message_id = "Не существует таска с таким id"
            self.error_message += f"{self.message_id}: {self.task_id}\n"
        if task_text is not None:
            self.task_text = task_text
            self.message_text = "Не существует таска с таким полем текста"
            self.error_message += f"{self.message_text}: {self.task_text}\n"

    def __str__(self):
        """
        Строковое представление ошибки
        :return: str: Текст ошибки
        """
        return self.error_message


class TaskCompletedException(Exception):
    """
    Пользовательское исключение вызываемое при попытке завершения завершенного таска
    """
    def __init__(self, id) -> None:
        """
        Инициализатор исключения
        :param id:
        """
        self.error_message = f"Таск {id} уже завершен"

    def __str__(self):
        return self.error_message
