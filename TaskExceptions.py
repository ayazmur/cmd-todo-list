class TaskExistingException(Exception):
    def __init__(self, id=None, task_text=None):
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
        return self.error_message


class TaskCompletedException(Exception):
    def __init__(self, id):
        self.error_message = f"Таск {id} уже завершен"

    def __str__(self):
        return self.error_message
