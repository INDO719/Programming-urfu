

class Transport:
    """
    Базовый класс транспорта.

    Attributes:
        name (str): Название транспорта.
    """

    def __init__(self, name: str) -> None:
        """
        Инициализирует транспорт.

        Args:
            name (str): Название транспорта.

        Returns:
            None
        """

        self.name = name

    def description(self) -> str:
        """
        Возвращает описание транспорта.

        Returns:
            str: Строка с описанием транспорта.

        Example:
            >>> Transport("Generic").description()
            'Транспорт - Generic'
        """

        return f"Транспорт - {self.name}"


class Car(Transport):
    """
    Автомобиль.

    Attributes:
        horsepower (float): Мощность автомобиля в лошадиных силах.
    """

    def __init__(self, name: str, horsepower: float) -> None:
        """
        Инициализирует автомобиль.

        Args:
            name (str): Название автомобиля.
            horsepower (float): Мощность в лошадиных силах.

        Returns:
            None
        """

        super().__init__(name)
        self.horsepower = horsepower

    def description(self) -> str:
        """
        Возвращает описание автомобиля.

        Returns:
            str: Строка с названием и мощностью автомобиля.
        """

        return f"Машина - {self.name} | Лошадиные силы - {self.horsepower}"


class Plane(Transport):
    """
    Самолёт.

    Attributes:
        vehicle_capacity (float): Максимальная вместимость.
    """

    def __init__(self, name: str, vehicle_capacity: float) -> None:
        """
        Инициализирует самолёт.

        Args:
            name (str): Название самолёта.
            vehicle_capacity (float): Максимальная вместимость.

        Returns:
            None
        """

        super().__init__(name)
        self.vehicle_capacity = vehicle_capacity

    def description(self) -> str:
        """
        Возвращает описание самолёта.

        Returns:
            str: Строка с названием и максимальной вместимостью.
        """

        return f"Самолет - {self.name} | Максимальная вместимость - {self.vehicle_capacity}"


class Bike(Transport):
    """
    Мотоцикл / байк.

    Attributes:
        speed (float): Максимальная скорость.
    """

    def __init__(self, name: str, speed: float) -> None:
        """
        Инициализирует байк.

        Args:
            name (str): Название байка.
            speed (float): Максимальная скорость.

        Returns:
            None
        """

        super().__init__(name)
        self.speed = speed

    def description(self) -> str:
        """
        Возвращает описание байка.

        Returns:
            str: Строка с названием и максимальной скоростью.
        """

        return f"Байк - {self.name} | Максимальная скорость - {self.speed}"


def print_info(object: Transport):
    return object.description()

toyota = Car("Toyota", 200)
airbus = Plane("Airbus A305", 150)
yamaha = Bike("Yamaha MT-09", 240)

print(print_info(toyota))
print(print_info(airbus))
print(print_info(yamaha))

