from uuid import UUID
from abc import ABC, abstractmethod


class AbstractDBManager(ABC):
    """
    Интерфейс для работы с базами данных
    """

    @abstractmethod
    def print_tasks(self) -> None:
        """
        Вывод всех тасков в консоль
        :return: None
        """
        pass

    @abstractmethod
    def add_task(self, text: str) -> None:
        """
        Создание нового таска
        :param text: Текст нового таска
        :return: None
        """
        pass

    @abstractmethod
    def edit_task(self, uid: UUID, text: str) -> None:
        """
        Редактирование таска
        :param uid: uid редактируемого таска
        :param text: Новый текст редактируемого таска
        :return: None
        """
        pass

    @abstractmethod
    def mark_done(self, uid: UUID) -> None:
        """
        Завершение задачи
        :param uid: uid завершаемого таска
        :return: None
        """
        pass

    @abstractmethod
    def delete_task(self, uid: UUID) -> None:
        """
        Удаление таска
        :param uid: uid удаляемого таска
        :return: None
        """
        pass
