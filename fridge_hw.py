import datetime
from decimal import Decimal
from typing import Optional


DATE_FORMAT = "%Y-%m-%d"

def add(items: dict[str, list],
        title: str,
        amount: Optional[float | int],
        expiration_date: Optional[str | None]=None) -> None:

    if title not in items:
        items[title] = []

    if expiration_date:
        expiration_date = datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()

    info = {"amount": Decimal(amount), "expiration_date": expiration_date}
    items[title].append(info)

def add_by_note(items: dict[str, list],
                note: str) -> None:

    note = note.split()
    expiration_date = None

    if '-' in note[-1]:
        expiration_date = note.pop()

    amount = note[-1]
    title = " ".join(note[:-1])

    add(items, title, amount, expiration_date)


def find(items: dict[str, list],
         needle: str) -> list[str]:

    needle = needle.lower()

    result = []

    for item in items.keys():
        if needle in item.lower():
            result.append(item)

    return result

def amount(items: dict[str, list],
           needle: str) -> Decimal:

    needle = needle.lower()

    list_of_needles = find(items, needle)

    result = Decimal('0')
    for item in list_of_needles:

        for batch in items[item]:
            result += batch["amount"]

    return result


"""def get_expired(items: dict[str, list], in_advance_days: int=0) -> dict[str, list]:
    today = datetime.date.today()
    expiration_date = today + datetime.timedelta(in_advance_days)

    products = {product: [] for product, batches in items.items()}

    for product, batches in items.items():
        for batch in batches:
            if batch['expiration_date'] is None:
                continue

            if batch['expiration_date'] < expiration_date:
                products[product].append(batch)
        if not products[product]:
            del products[product]

    return products"""


def get_expired(items, in_advance_days=0):
    today = datetime.date.today()
    expiration_date = today + datetime.timedelta(in_advance_days)

    products = []

    for product, batches in items.items():
        lst_batch = []
        for batch in batches:
            if batch['expiration_date'] is None:
                continue

            if batch['expiration_date'] <= expiration_date:
                lst_batch.append(batch['amount'])
        if len(lst_batch) != 0:
            products.append((product, sum(lst_batch)))

    return products

def main():

    goods = {'Яйца Фабрики №1': [{'amount': Decimal('1'),
                      'expiration_date': datetime.date(2026, 10, 15)}],
 'Фабрика №2: яйца': [{'amount': Decimal('2'),
                       'expiration_date': datetime.date(2026, 10, 11)},
                      {'amount': Decimal('3'),
                       'expiration_date': datetime.date(2026, 10, 13)}],
 'макароны': [{'amount': Decimal('100'), 'expiration_date': None}]}


    print(get_expired(goods))

if __name__ == '__main__':
    main()

