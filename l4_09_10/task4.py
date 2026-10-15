"""Задача #4 – сложные пароли"""


import string
import random
from typing import Optional

def generate_password(length: int, lowercase: bool,
                      uppercase: bool, special: bool, nums: bool) -> Optional[str | None]:
    if length == 0:
        print("Вы не указали длину")
        return

    alph = ""
    if lowercase:
        alph += string.ascii_lowercase
    if uppercase:
        alph += string.ascii_uppercase

    if special:
        alph += "!@#$%^&*()_"

    if nums:
        alph += "0123456789"

    if not alph:
        print("Пароль должен содержать символы.")
        return

    password = "".join([random.choice(alph) for _ in range(length)])

    return password

print("Сгенерируйте свой пароль")
length_pass = int(input("Введите длину пароля: "))
lower_pass = input("В пароле будет нижний регистр? (да/нет): ")
upper_pass = input("В пароле будет верхний регистр?(да/нет): ")
spec_pass = input("В пароле будут специальные символы?(да/нет): ")
nums_pass = input("В пароле будут цифры?(да/нет): ")

is_lower = lower_pass == "да"
is_upper = upper_pass == "да"
is_spec = spec_pass == "да"
is_nums = nums_pass == "да"

password = generate_password(length_pass, is_lower, is_upper, is_spec, is_nums)
if password is not None:
    print(f"Ваш пароль: {password}")