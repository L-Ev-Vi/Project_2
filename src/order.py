from src.base_category_order import BaseCategoryOrder
from src.error_when_adding_a_product import ErrorAddingAnEmptyValue, ProductNameErrorWhenAdding


class Order(BaseCategoryOrder):
    """Класс для определения объекта-заказа, в котором хранится информация, о том какой товар был куплен,
    количество купленного товара, а также итоговая стоимость.
    При этом в одном заказе может быть указан только один товар."""

    __ID_ORDER = 1  # ID заказа
    __order_count = 0  # количество заказов
    __number_products_sold = 0  # количество проданных товаров

    __name_product: str  # название товара
    description: str  # описание заказа
    __price: float  # цена товара
    quantity: int  # количество в наличии

    def __init__(self, name_product: str, description: str, price: float, quantity: int) -> None:
        """Метод для инициализации объекта-класса 'Заказ'."""
        try:
            self.__id = self.__ID_ORDER
            self.__name_product = name_product
            self.description = description
            self.__price = price * quantity
            if quantity <= 0:
                raise ErrorAddingAnEmptyValue
            self.quantity = quantity
            Order.__ID_ORDER += 1
            Order.__order_count += 1
            Order.__number_products_sold += quantity
        except ErrorAddingAnEmptyValue as e:
            print(e)
        else:
            print("Товар добавлен.")
        finally:
            print("Обработка добавления товара завершена.")

    def __str__(self) -> str:
        """Магический метод, который отображает информацию заказа, о том какой товар был куплен,
        в каком количестве и какова итоговая стоимость заказа."""
        return (
            f"Заказ №{self.__id}, Товар: {self.__name_product}, {self.description}, в количестве: {self.quantity} шт.,"
            f" стоимостью: {self.__price}"
        )

    def add_product(self, name_new_product: str, price: float, quantity: int) -> None:
        """Метод для добавления товара в заказ. Метод проверяет добавляемый товар с уже существующим в заказе,
        в случае совпадения, увеличивает количество покупаемого товара.
        В другом случае добавляемый товар игнорируется"""
        try:
            if self.__name_product == name_new_product:
                if quantity <= 0:
                    raise ErrorAddingAnEmptyValue
                self.quantity += quantity
                self.__price += price * quantity
                Order.__number_products_sold += quantity
            else:
                raise ProductNameErrorWhenAdding
        except ErrorAddingAnEmptyValue:
            print("Не указанно количество товара")
        except ProductNameErrorWhenAdding:
            print(f"Для товара {name_new_product} необходимо сформировать отдельный заказ")
        else:
            print("Товар добавлен.")
        finally:
            print("Обработка добавления товара завершена.")

    @property
    def products(self) -> str:
        """Гетер который возвращает информацию об объекте-класса (заказе)."""
        return f"{self.__str__()}\n"
