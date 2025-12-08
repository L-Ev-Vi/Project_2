from typing import Any


class ErrorWhenAddingAProduct(Exception):
    """Класс исключения, который отвечает за обработку событий,
    когда в «Категорию» или «Заказ» добавляется товар"""

    def __init__(self, *args: Any) -> None:
        """Метод для инициализации текста исключения."""
        self.message = args[0] if args else "Общая ошибка при добавлении товара"

    def __str__(self) -> str:
        return self.message


class ErrorAddingAnEmptyValue(ErrorWhenAddingAProduct):
    """Класс исключения, который отвечает за обработку событий,
    когда в «Категорию» или «Заказ» добавляется товар с нулевым количеством"""

    def __init__(self, *args: Any) -> None:
        """Метод для инициализации текста исключения."""
        self.message = args[0] if args else "Попытка добавить товар с нулевым количеством"


class ProductNameErrorWhenAdding(ErrorWhenAddingAProduct):
    """Класс исключения, который отвечает за обработку событий,
    когда в «Категорию» или «Заказ» добавляется товар с не схожим названием"""

    def __init__(self, *args: Any) -> None:
        """Метод для инициализации текста исключения."""
        self.message = args[0] if args else "Не схожее имя товара"
