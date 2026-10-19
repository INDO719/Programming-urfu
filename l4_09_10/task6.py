"""Задача #6 – виселица"""

import random


words = ["саламандра"]

attempts = [
    [(6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0), (6, 8), (5, 8), (4, 8), (3, 8), (2, 8), (1, 8), "|", 1],
    [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), "_", 1],
    [(1, 4), (2, 4), "|", 1],
    [(3, 3), (3, 5), "(", ")", 2],
    [(4, 4), "|", 1],
    [(4, 3), (4, 5), "/", chr(92), 2],
    [(5, 3), (5, 5), "/", chr(92), 2]
]

def game() -> None:
    """
        Запускает игру «Виселица»

        Загадывает случайное слово, принимает буквы от пользователя,
        отображает текущее состояние слова и виселицы. Игра заканчивается
        победой при угадывании всех букв или поражением после исчерпания попыток.

        Returns:
            None: Функция ничего не возвращает, только взаимодействует с пользователем

        Example:
            >>> game()  # запускает интерактивную игру
    """

    gal = make_gal()
    word = random.choice(words)
    att = 0

    try_word = ["*" for _ in range(len(word))]
    print("Угадайте слово и не умрите!")

    while att != len(attempts):

        print("\n" + "_" * len(word))
        print("".join(try_word))
        print("_" * len(word))

        if winner(word, try_word):
            print("Победа!")
            break

        letter = input("Назовите букву: ")

        if letter in try_word:
            print("Эта буква уже была")
            continue

        idx = check(letter, word)

        if idx:
            for i in idx:
                try_word[i] = letter
        else:
            att += 1
            gal = change_gallows(att, gal)

        if att != 0:
            print_gal(gal)

    print("Вы проиграли и умерли }:(")


def winner(word: str, try_word: list[str]) -> bool:
    """
        Проверяет, угадано ли слово полностью

        Args:
            word (str): Загаданное слово
            try_word (list[str]): Текущее состояние угадывания (буквы и символы '*')

        Returns:
            bool: True, если все буквы угаданы, иначе False

        Example:
            >>> winner("кот", ["к", "о", "т"])
            True
    """

    return word == "".join(try_word)


def check(let: str, word: str) -> list[int]:
    """
        Находит позиции буквы в загаданном слове

        Args:
            let (str): Проверяемая буква
            word (str): Загаданное слово

        Returns:
            list[int]: Список индексов, где встречается буква; пустой список, если буквы нет

        Example:
            >>> check("а", "саламандра")
            [1, 3, 5, 9]
    """

    return [i for i in range(len(word)) if word[i] == let.lower()]


def change_gallows(att: int, gal: list[list[str]]) -> list[list[str]]:
    """
        Добавляет на виселицу следующую часть по номеру неудачной попытки

        Args:
            att (int): Номер текущей неудачной попытки (начиная с 1)
            gal (list[list[str]]): Текущее изображение виселицы

        Returns:
            list[list[str]]: Обновлённое изображение виселицы
    """

    att -= 1

    attempt = attempts[att]
    quantity = attempt.pop()

    if quantity == 1:
        for coords in attempt[:-1]:
            gal[coords[0]][coords[1]] = attempt[-1]

    if quantity == 2:
        coord1 = attempt[0]
        coord2 = attempt[1]
        gal[coord1[0]][coord1[1]] = attempt[2]
        gal[coord2[0]][coord2[1]] = attempt[3]

    return gal

def print_gal(gal: list[list[str]]) -> None:
    """
        Выводит изображение виселицы в консоль

        Args:
            gal (list[list[str]]): Изображение виселицы

        Returns:
            None: Функция ничего не возвращает, только печатает изображение
    """

    for row in gal:
        print("".join(row))

def make_gal() -> list[list[str]]:
    """
        Создаёт пустое изображение виселицы

        Returns:
            list[list[str]]: Двумерный список 7x9, заполненный пробелами
    """

    return [[" " for _ in range(9)] for _ in range(7)]


if __name__ == "__main__":
    game()