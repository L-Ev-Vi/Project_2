from abc import ABC, abstractmethod
from typing import Any


class BaseCategoryOrder(ABC):
    """Базовый абстрактный класс для подкласса Category и Order"""

    @abstractmethod
    def add_product(self, *args: Any, **kwargs: Any) -> None:
        """Абстрактный метод, для добавления товара"""

    # в методе необходимо реализовать логику по добавлению объекта класса Product

    @property
    @abstractmethod
    def products(self) -> str:
        """Абстрактный метод для отображения информации"""

    # в данном методе реализуется вывод информации для пользователя
