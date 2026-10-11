"""Задача #3 – пироженки и коробочки"""


def print_pack_report(amount: int) -> None:

    for n in range(amount, 0, -1):
        pass

    is_3 = amount % 3 == 0
    is_5 = amount % 5 == 0

    if is_3 and is_5:
        print(f"{amount} - расфасуем по 3 или по 5")
    elif is_3:
        print(f"{amount} - расфасуем по 3")
    elif is_5:
        print(f"{amount} - расфасуем по 5")
    else:
        print(f"{amount} - не заказываем!")

print_pack_report(30)
print_pack_report(6)
print_pack_report(55)
print_pack_report(13)
