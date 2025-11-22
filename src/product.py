class Product:
    """Клас для определения товаров их кратких характеристик, ценны и количества."""

    name: str  # название товара
    description: str  # описание товара
    price: float  # цена товара
    quantity: int  # количество в наличии

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Метод для инициализации класса Товар."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
