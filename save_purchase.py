from sqlite3 import connect
import csv
from create import superheroes, items, branches
from dataclasses import dataclass


@dataclass
class Purchase:
    date: str
    time: str
    superhero_id: int
    item_id: int
    branch_id: int

    def sql_exe(self) -> str:
        res = f"""
INSERT INTO Purchase(
        date,
        time,
        superhero_id,
        item_id,
        branch_id
    )
VALUES(
        "{self.date}",
        "{self.time}",
        "{self.superhero_id}",
        "{self.item_id}",
        "{self.branch_id}"
    );
        """
        return res


superheroes_list = [n.name for n in superheroes.values()]
items_list = [n.name for n in items.values()]
branches_list = [n.name for n in branches.values()]


with connect("test.sqlite3") as connection:

    with open("data/combined_edited.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            purchase = Purchase(
                row["date"],
                row["time"],
                superheroes_list.index(row["customer"]) + 1,
                items_list.index(row["item"]) + 1,
                branches_list.index(row["branch"]) + 1,
            )
            exe = purchase.sql_exe()
            cursor = connection.execute(exe)
