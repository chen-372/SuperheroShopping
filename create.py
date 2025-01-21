import random
from dataclasses import dataclass


def random_superhero() -> Superhero:
    key = random.randint(1, 8)
    return superheroes[key]


def random_branch() -> Branch:
    key = random.randint(1, 8)
    return branches[key]


def random_item() -> Item:
    key = random.randint(1, 8)
    return items[key]


def random_time() -> str:
    hh = str(sum([random.randint(1, 6) for _ in range(4)]) % 24).rjust(2, "0")
    mm = str(random.randint(1, 6) % 6) + str(
        (random.randint(1, 6) + random.randint(1, 6)) % 10
    )
    return f"{hh}:{mm}"


def random_transaction(date: str) -> list[str]:
    customer = random_superhero()
    item = random_item()
    branch = random_branch()
    time = random_time()
    dt = [
        date,
        time,
        customer.name,
        customer.true_identity,
        customer.address,
        customer.telephone,
        customer.email,
        customer.date_of_birth,
        item.name,
        item.price,
        item.weight,
        item.department,
        item.supplier,
        branch.name,
        branch.address,
        branch.telephone,
        branch.email,
        branch.manager,
    ]
    return dt


def random_data() -> list[list[str]]:
    dt = []
    for date in range(1, 31):
        trans_num = random.randint(1, 8)
        for _ in range(trans_num):
            dt.append(random_transaction(f"{date} November"))
    return dt


def print_file(dt: list[list[str]]) -> None:
    for row in dt:
        print('"' + '","'.join(row) + '"')


if __name__ == "__main__":
    print_file(random_data())
