from datetime import datetime

from abc import ABC, abstractmethod


class Printable(ABC):
    """Абстрактный интерфейс для объектов, умеющих выводить информацию о себе."""
    @abstractmethod
    def info(self):
        """
        Возвращает строковое описание объекта.

        Returns:
            str: Текстовое описание объекта.
        """

        pass


class Book(Printable):
    """
    Книга.

    Attributes:
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания.
    """

    @classmethod
    def make_from_string(cls, data: str):
        """
        Создаёт книгу из строки формата ``'название;автор;год'``.

        Args:
            data (str): Строка с данными книги, разделёнными точкой с запятой.

        Returns:
            Book: Новый экземпляр книги.
        """
        title, author, year = data.split(";")
        return cls(title, author, int(year))

    def __init__(self, title: str, author: str, year: int) -> None:
        """
        Инициализирует книгу.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания.

        Returns:
            None
        """

        self.title = title
        self.author = author
        self.year = year

    def info(self) -> str:
        """
        Возвращает строковое описание книги.

        Returns:
            str: Название, автор и год издания.

        Example:
            >>> Book("Остров", "Бил не Гейтс", 2015).info()
            'Название: Остров | Автор: Бил не Гейтс | Год: 2015'
        """

        return f"Название: {self.title} | Автор: {self.author} | Год: {self.year}"

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.

        Returns:
            str: То же, что и info.
        """

        return self.info()

    def __eq__(self, other) -> bool:
        """
        Сравнивает книги по названию и автору.

        Args:
            other (object): Другой объект для сравнения.

        Returns:
            bool: ``True``, если ``other`` — книга с такими же названием и автором.

        Example:
            >>> Book("Остров", "Бил не Гейтс", 2015) == Book("Остров", "Бил не Гейтс", 2016)
            True
        """

        return isinstance(self, Book) and self.title == other.title and self.author == self.author

    @property
    def age(self) -> int:
        """
        Возвращает возраст книги в годах.

        Returns:
            int: Разница между текущим годом и годом издания.
        """

        return datetime.now().year - self.year

    @age.setter
    def age(self, value) -> None:
        """
        Устанавливает год издания на основе возраста книги.

        Args:
            value (int): Желаемый возраст книги в годах.

        Returns:
            None
        """

        self.year = datetime.now().year - value


class Ebook(Book):
    """
    Электронная книга.

    Attributes:
        format (str): Формат электронной книги.
    """

    def __init__(self, title: str, author: str, year: int, format: str) -> None:
        """
        Инициализирует электронную книгу.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания.
            format (str): Формат электронной книги.

        Returns:
            None
        """

        super().__init__(title, author, year)
        self.format = format

    def info(self) -> str:
        """
        Возвращает строковое описание электронной книги.

        Returns:
            str: Название, автор, год издания и формат.
        """

        return f"Название: {self.title} | Автор: {self.author} | Год: {self.year} | Формат: {self.format}"



book1 = Book("Остров", "Бил не Гейтс", 2015)
book2 = Book.make_from_string("Остров;Бил не Гейтс;2015")
print(book1.info())
print(book2)


ebook1 = Ebook("Пингвины", "Косатков", 1950, "А4")
ebook2 = Ebook("Пингвины", "Косатков", 1950, "А4")
print(ebook1.info())
print(ebook1 == ebook2)



