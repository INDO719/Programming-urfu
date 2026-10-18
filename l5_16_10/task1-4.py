from datetime import datetime

from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def info(self):
        pass


class Book(Printable):
    @classmethod
    def make_from_string(cls, data: str):
        title, author, year = data.split(";")
        return cls(title, author, int(year))

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def info(self) -> str:
       return f"Название: {self.title} | Автор: {self.author} | Год: {self.year}"

    def __str__(self):
        return self.info()

    def __eq__(self, other):
        return isinstance(self, Book) and self.title == other.title and self.author == self.author

    @property
    def age(self):
        return datetime.now().year - self.year

    @age.setter
    def age(self, value):
        self.year = datetime.now().year - value


class Ebook(Book):
    def __init__(self, title: str, author: str, year: int, format: str):
        super().__init__(title, author, year)
        self.format = format

    def info(self):
        return f"Название: {self.title} | Автор: {self.author} | Год: {self.year} | Формат: {self.format}"



book1 = Book("Остров", "Бил не Гейтс", 2015)
book2 = Book.make_from_string("Остров;Бил не Гейтс;2015")
print(book1.info())
print(book2)


ebook1 = Ebook("Пингвины", "Косатков", 1950, "А4")
ebook2 = Ebook("Пингвины", "Косатков", 1950, "А4")
print(ebook1.info())
print(ebook1 == ebook2)



