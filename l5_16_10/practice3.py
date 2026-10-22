import datetime
from math import floor


class Product:
    def __init__(self, name: str, price: float, presence: bool, category: str, discount: int = 0) -> None:
        self.name = name
        self.price = price
        self.presence = presence
        self.category = category
        self.discount = discount

    def get_info(self) -> str:
        return (f"Product - {self.name} | "
                f"Price - {self.price} | "
                f"In stock - {"yes" if self.presence else "no" }"
                f"{f" | Discount - {self.discount}%" if self.discount else ""}")


class ShoppingCart:
    def __init__(self) -> None:
        self.cart: list[Product] = []

    def add_product(self, *args: Product) -> None:
        for product in args:
            self.cart.append(product)

    def delite_product(self, product: Product) -> None:
        if product not in self.cart:
            print("There is no such product")

        self.cart.remove(product)

    def update_shopping_cart(self) -> None:
        self.cart.clear()


class Order:
    tax = 13

    def __init__(self, shopping_cart: ShoppingCart) -> None:
        self.products: list[Product] = shopping_cart.cart

    def calculate_price(self) -> float:
        price = sum(product.price * (1 - product.discount / 100) for product in self.products if product.presence)
        return round(price * (1 + self.tax / 100), 2)

    def get_info(self) -> str:
        products = [product.get_info() for product in self.products if product.presence]
        final_price = self.calculate_price()

        if not products:
            return "Shopping cart is empty"

        return "ORDER:\n - " + "\n - ".join(products) + f"\nTax - {self.tax}%" + f"\nPrice - {final_price}"


class Customer:
    def __init__(self, name: str, birth_date: datetime.date) -> None:
        self.name = name
        self.birth_date = birth_date

        self.shopping_cart = ShoppingCart()
        self.order_history = []

    def make_shopping_cart(self, *args: Product) -> None:
        self.shopping_cart.update_shopping_cart()

        self.shopping_cart.add_product(*args)

    def add_history(self, order: Order) -> None:
        self.order_history.append(order.get_info())

    def show_history(self) -> str:
        return "\n\n".join(self.order_history)

    def get_age(self) -> int:
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


