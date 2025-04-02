class Task:
    """
    Класс таска для использования в базе данных JSON
    """
    def __init__(self, name):
        """
        Инициализатор для экземпляра таска
        :param name: текст таска
        """
        self.name = name
        self.active = True
