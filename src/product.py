from typing import Any


class Product:
    """Клас для определения товаров их кратких характеристик, ценны и количества."""

    name: str  # название товара
    description: str  # описание товара
    _price: float  # цена товара
    quantity: int  # количество в наличии

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Метод для инициализации класса Товар."""
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_parameters: dict, list_products: list = None) -> Any:
        """Класс-метод который принимает на вход параметры товара в словаре,
        и возвращать созданный объект класса Product. Также метод может проводить проверку наличия такого же товара
        схожего по имени, и в случае если товар уже существует, то количество старого товара и нового суммируется.
        При конфликте цен выбирается та цена которая является более высокой.
        Для этого можно в метод передать не обязательный параметр в виде списка товаров,
        в котором нужно искать дубликаты."""
        if list_products:
            new_product = cls(**product_parameters)
            for product in list_products:
                if product.name == new_product.name:
                    product.quantity += new_product.quantity
                    if product._price < new_product._price:
                        product._price = new_product._price
                    return product
                else:
                    return cls(**product_parameters)
        else:
            return cls(**product_parameters)

    @property
    def price(self) -> float | int:
        """Гетер который возвращает цену товаров в виде числа"""
        return self._price

    @price.setter
    def price(self, new_price: float | int) -> str | None:
        """Cеттер который реализует проверку новой цены продукта: в случае если цена товара равна или ниже нуля,
        выводите сообщение в консоль “Цена не должна быть нулевая или отрицательная”,
        при этом новая цена не устанавливается. В случае если новая цена товара ниже установленной ранее,
        отправляется запрос подтверждения пользователем вручную через ввод где 'y' или 'Y' (значит yes)
        согласие понизить цену, а любой другой вариант вода (значит no) отмена действия соответственно."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif self._price > new_price:
            confirmation = input("Новая цена товара ниже установленной ранее, подтвердить ввод? "
                                 "'Y'(значит yes) / 'N'(значит no)\n->")
            if confirmation.lower() == "y":
                self._price = new_price
        else:
            self._price = new_price
