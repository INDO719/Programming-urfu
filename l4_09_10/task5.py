"""Задача #5 – римский конвертер"""


alph_rn = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900,
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

alph_nr = {value: key for key, value in alph_rn.items()}


def from_roman_to_numeral_converter(number: str) -> int:
    """
        Преобразует римское число в целое число

        Args:
            number (str): Римское число в виде строки

        Returns:
            int: Целое число, соответствующее римскому числу

        Example:
            >>> from_roman_to_numeral_converter("XIV")
            14
    """

    result = 0

    for sym in number[:]:
        if sym in ("IV", "IX", "XL", "XC",  "CD", "CM"):
            result += alph_rn[sym]
            number = number.replace(alph_rn[sym], "")

    for sym in number:
        result += alph_rn[sym]

    return result

def from_numeral_to_roman_converter(number: int) -> str:
    """
        Преобразует целое число в римское число

        Args:
            number (int): Целое число для преобразования (не больше 3999)

        Returns:
            str: Римское представление числа

        Raises:
            ValueError: Если число больше 3999

        Example:
            >>> from_numeral_to_roman_converter(14)
            'XIV'
    """

    if number > 3999:
        raise ValueError("Нельзя передавать числа большие 3999")

    result = ""

    for dec in range(1, 5):
        rem = number % 10 ** dec

        if rem == 0:
            continue
        elif rem in (4, 9, 40, 90, 400, 900):
            result += alph_nr[rem]
            number -= rem
        else:
            if rem / 10 ** (dec - 1) > 5:
                result += alph_nr[5 * 10 ** (dec - 1)]
                rem -= 5 * 10 ** (dec - 1)

            result += alph_nr[10 ** (dec - 1)] * (rem // 10 ** (dec - 1))

    return result[::-1]


print(from_roman_to_numeral_converter("MMMXXXL"))
print(from_numeral_to_roman_converter(3080))