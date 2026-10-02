#1------------------------------------------------------------

tempC = 12
tempF = (tempC * 9 / 5) + 32
tempK = tempC + 273.15
print(f"{tempF:.2f}")
print(f"{tempK:.2f}")


#2------------------------------------------------------------

n = 50 # int(input())

print("True" if n % 2 == 0 else "False")

if n > 0:
    print("+")
elif n < 0:
    print("-")
else:
    print("0")

print("True" if n in range(10, 50 + 1) else "False")


#3------------------------------------------------------------

import string
import random

let = string.ascii_uppercase
sp_s = "!@#$%^&*"
password = []
for _ in range(3):
    password.append(random.choice(let))
    password.append(str(random.randint(0, 10)))
for _ in range(2):
    password.append(random.choice(sp_s))
random.shuffle(password)
password = "".join(password)
print(password)


#4------------------------------------------------------------

from collections import Counter

user_string = "ewre" #input().lower()
us_count = Counter(user_string)

print(us_count.most_common(3))


#5------------------------------------------------------------

def r_e(rng: list) -> list:
    result = []
    while len(rng) > 0:
        n = rng.pop(0)
        result.append(n)
        rng = [x for x in rng if x % n != 0]
    return result

N = 100
rng = list(range(2, N + 1))
print(r_e(rng))


#6------------------------------------------------------------

# Функция, которая определяет скажем степень 10, например для 4000 это 3 ведь 10^3 == 1000
def define_power(n: int) -> int:
    pow = 1
    while 10**pow <= n:
        pow += 1
    return pow - 1

def solution(n:int) -> int:
    pow = define_power(n)

    # На числах после, больших 10^100 заметил, что приходится расширять диапазон кандидатов для отрезка, причем это приходится делать каждые 10^100
    powl = pow - pow // 100
    powr = pow + pow // 100 + 4
    lst_candidates = {
        int(((9 * i - 10) * 10 ** (i - 1) + 1)) // 9: i - 1
        for i in range(powl, powr)
    }


    if n in lst_candidates:
        return int(str(10**lst_candidates[n] - 1)[-1])

    # Определяем промежуток в котором находится цифра в строке
    r_s = [c for c in lst_candidates.keys() if n < c][0]
    l_s = [c for c in lst_candidates.keys() if n > c][-1]
    rng_s = [l_s, r_s]

    # Определяем промежуток в котором находится число с искомой цифрой
    pow_l = lst_candidates[rng_s[0]]
    pow_r = lst_candidates[rng_s[1]]

    rng_n = [10**pow_l, 10**pow_r]

    # Вычисляем сколько нужно прибавить к началу промежутка чисел, чтобы получить число близкое к числу с искомой цифрой
    c = (n - rng_s[0] - 1) // pow_r - 1
    c = c if c >= 0 else 0

    right_b = rng_n[0] + c

    right_s = rng_s[0] + 1 + c * pow_r

    # Берем небольшой промежуток цифр и формируем строку
    x1 = right_b
    x2 = x1 + 4
    string = list("".join([str(x) for x in range(x1, x2 + 1)]))

    # Нумеруем каждую цифру из строки начиная с right_s
    y = list(map(int, string))
    x = [x + right_s for x in range(len(y))]

    # Делаем словарь номер: цифра
    result = {x[i]: y[i] for i in range(len(x))}

    return result[n]

n = 12312312# Любое число, которое может обработать python
print(solution(n))