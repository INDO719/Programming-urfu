import datetime
from math import floor


class Product:
    """
    Товар в магазине.

    Attributes:
        name (str): Название товара.
        price (float): Цена товара.
        presence (bool): Наличие товара.
        category (str): Категория товара.
        discount (int): Скидка в процентах.
    """

    def __init__(self, name: str, price: float, presence: bool, category: str, discount: int = 0) -> None:
        """
        Инициализирует товар.

        Args:
            name (str): Название товара.
            price (float): Цена товара.
            presence (bool): Наличие товара.
            category (str): Категория товара.
            discount (int, optional): Скидка в процентах. По умолчанию 0.

        Returns:
            None
        """

        self.name = name
        self.price = price
        self.presence = presence
        self.category = category
        self.discount = discount

    def get_info(self) -> str:
        """
        Возвращает строковое описание товара.

        Returns:
            str: Описание товара с ценой, наличием и скидкой.
        """

        return (f"Product - {self.name} | "
                f"Price - {self.price} | "
                f"In stock - {"yes" if self.presence else "no" }"
                f"{f" | Discount - {self.discount}%" if self.discount else ""}")


class ShoppingCart:
    """
    Корзина покупателя.

    Attributes:
        cart (list[Product]): Список товаров в корзине.
    """

    def __init__(self) -> None:
        """
        Инициализирует пустую корзину.

        Returns:
            None
        """

        self.cart: list[Product] = []

    def add_product(self, *args: Product) -> None:
        """
        Добавляет товары в корзину.

        Args:
            *args (Product): Товары для добавления.

        Returns:
            None
        """

        for product in args:
            self.cart.append(product)

    def delite_product(self, product: Product) -> None:
        """
        Удаляет товар из корзины.

        Args:
            product (Product): Товар для удаления.

        Returns:
            None
        """

        if product not in self.cart:
            print("There is no such product")
            return

        self.cart.remove(product)

    def update_shopping_cart(self) -> None:
        """
        Очищает корзину.

        Returns:
            None
        """

        self.cart.clear()


class Order:
    """
    Заказ, сформированный на основе корзины.

    Attributes:
        tax (int): Процент налога.
        products (list[Product]): Товары в заказе.
    """

    tax = 13

    def __init__(self, shopping_cart: ShoppingCart) -> None:
        """
        Инициализирует заказ на основе корзины.

        Args:
            shopping_cart (ShoppingCart): Корзина с товарами.

        Returns:
            None
        """

        self.products: list[Product] = shopping_cart.cart

    def calculate_price(self) -> float:
        """
        Вычисляет итоговую стоимость заказа с учётом скидок и налога.

        Returns:
            float: Итоговая стоимость заказа.
        """

        price = sum(product.price * (1 - product.discount / 100) for product in self.products if product.presence)
        return round(price * (1 + self.tax / 100), 2)

    def get_info(self) -> str:
        """
        Возвращает строковое описание заказа.

        Returns:
            str: Описание заказа или сообщение о пустой корзине.
        """

        products = [product.get_info() for product in self.products if product.presence]
        final_price = self.calculate_price()

        if not products:
            return "Shopping cart is empty"

        return "ORDER:\n - " + "\n - ".join(products) + f"\nTax - {self.tax}%" + f"\nPrice - {final_price}"


class Customer:
    """
    Покупатель.

    Attributes:
        name (str): Имя покупателя.
        birth_date (datetime.date): Дата рождения.
        shopping_cart (ShoppingCart): Корзина покупателя.
        order_history (list[str]): История заказов в виде строк.
    """

    def __init__(self, name: str, birth_date: datetime.date) -> None:
        """
        Инициализирует покупателя.

        Args:
            name (str): Имя покупателя.
            birth_date (datetime.date): Дата рождения.

        Returns:
            None
        """

        self.name = name
        self.birth_date = birth_date

        self.shopping_cart = ShoppingCart()
        self.order_history = []

    def make_shopping_cart(self, *args: Product) -> None:
        """
        Формирует новую корзину из переданных товаров.

        Args:
            *args (Product): Товары для добавления в корзину.

        Returns:
            None
        """

        self.shopping_cart.update_shopping_cart()

        self.shopping_cart.add_product(*args)

    def add_history(self, order: Order) -> None:
        """
        Добавляет заказ в историю заказов.

        Args:
            order (Order): Заказ для добавления.

        Returns:
            None
        """

        self.order_history.append(order.get_info())

    def show_history(self) -> str:
        """
        Возвращает историю заказов.

        Returns:
            str: История заказов, разделённая пустыми строками.
        """

        return "\n\n".join(self.order_history)

    def get_age(self) -> int:
        """
        Вычисляет возраст покупателя.

        Returns:
            int: Возраст в полных годах.
        """

        return floor((datetime.datetime.now().date() - self.birth_date).days / 365.25)



bread = Product("Bread", 80, True, "rich")
milk = Product("Milk", 90, True, "lactic", 15)
cheese = Product("Cheese", 130, True, "fermented milk", 20)

cust = Customer("bob", datetime.date(2000, 1, 1))

cust.make_shopping_cart(bread, milk, cheese)

ord1 = Order(cust.shopping_cart)
ord2 = Order(cust.shopping_cart)
ord3 = Order(cust.shopping_cart)

cust.add_history(ord1)
cust.add_history(ord2)
cust.add_history(ord3)
print(cust.show_history())


