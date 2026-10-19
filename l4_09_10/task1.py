"""Задача #1 – шифр Цезаря"""


import string


RU_ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ANG_ALPHABET = string.ascii_uppercase


def caesar_cipher(message: str, step: int) -> str:
    """
    Шифрует сообщение шифром Цезаря

    Args:
    message (str): Сообщение для шифрования
    step (int): Шаг сдвига (может быть отрицательным)

    Returns:
    str: Зашифрованное сообщение

    Example:
        >>>caesar_cipher("Hello", 1)
        Ifmmp
    """

    encrypted_message = ""
    language = RU_ALPHABET if message[0].upper() in RU_ALPHABET else ANG_ALPHABET

    for let in message:
        if let == " ":
            encrypted_message += " "
            continue

        idx = language.index(let.upper()) + abs(step) % len(language) * (step // abs(step))
        if len(language) - 1:
            idx %= len(language)

        if let.isupper():
            encrypted_message += language[idx]
        else:
            encrypted_message += language[idx].lower()

    return encrypted_message


message = "Hello World"
shift = 1
x = caesar_cipher(message, shift)
print(f"{x} | {caesar_cipher(x, -shift)}")
