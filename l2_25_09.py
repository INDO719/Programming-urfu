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


