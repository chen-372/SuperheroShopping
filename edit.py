import csv


power = {
    "The Amazing Cockroach Man": "Scuttling around rubbish bins.",
    "The Incredible Sulk": "Sulking over predicted grades.",
    "Copper Man": "Conducting electricity.",
    "Blunder Woman": "Stubbing toes.",
    "Soup Man": "Slurping noodles.",
    "Batty Girl": "Saying inappropriate things.",
    "Splash": "Having quick showers.",
    "Captain Inner Mongolia": "Seeing across grasslands.",
}

# updates: dict[str, list] = {
#     "search column": ["customer", "customer", "item", "customer"],
#     "search value": ["Copper Man", "The Incredible Sulk", "Toilet Paper", "Soup Man"],
#     "update column": ["customer", "item price", "item price", "customer address"],
#     "update method": ["repl", "calc", "calc", "repl"],
#     "update value": ["Copper Woman", [0.9, "$ ~"], [1.5, "$ ~"], "Crazy Land"],
# }


def read_file(path: str) -> list[dict]:
    dt = []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            dt.append(row)

    return dt


def str2float(string: str) -> float:
    """remove comma"""
    string = string[2:]
    return float(string.replace(",", ""))


def float2str(num: float) -> str:
    string = str(num)
    dot = string.index(".")
    integer = string[:dot]
    f = string[dot:]
    sep = []
    temp = ""
    for i in range(len(integer) - 1, -1, -1):
        temp = integer[i] + temp
        if ((len(integer) - i) % 3 == 0 and i != len(integer) - 1) or i == 0:
            sep.insert(0, temp)
            temp = ""
    return "$ " + ",".join(sep) + f


def save_file(dt: list[dict], path: str) -> None:
    title = [
        "date",
        "time",
        "customer",
        "customer true identity",
        "customer address",
        "customer telephone",
        "customer email",
        "customer date_of_birth",
        "customer super power",
        "item",
        "item price",
        "item weight",
        "item department",
        "item supplier",
        "branch",
        "branch address",
        "branch telephone",
        "branch email",
        "branch manager",
    ]
    print('"' + '","'.join(title) + '"')
    for row in dt:
        print('"', end="")
        for i, t in enumerate(title):
            print(row[t], end='"')
            if i != len(title) - 1:
                print(',"', end="")
        print("")


if __name__ == "__main__":
    dt = read_file("combined.csv")
    for transaction in dt:

        transaction["customer super power"] = power[transaction["customer"]]

        if transaction["customer"] == "Copper Man":
            transaction["customer"] = "Copper Woman"

        if transaction["customer"] == "The Incredible Sulk":
            num = str2float(transaction["item price"])
            num = round(num * 0.9, 2)
            print(num)
            transaction["item price"] = float2str(num)

        if transaction["item"] == "Toilet Paper":
            num = str2float(transaction["item price"])
            num = round(num * 1.5, 2)
            transaction["item price"] = float2str(num)

        if transaction["customer"] == "Soup Man":
            transaction["customer address"] = "Crazy Land"

    save_file(dt, "")
