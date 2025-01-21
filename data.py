from dataclasses import dataclass


@dataclass
class Superhero:
    name: str
    address: str
    true_identity: str
    telephone: str
    email: str
    date_of_birth: str
    super_power: str

    def sql_exe(self) -> str:
        res = f"""
INSERT INTO Superhero(
        name,
        address,
        true_identity,
        telephone,
        email,
        date_of_birth,
        super_power
    )
VALUES(
        "{self.name}",
        "{self.address}",
        "{self.true_identity}",
        "{self.telephone}",
        "{self.email}",
        "{self.date_of_birth},
        "{self.super_power}"
    );
        """
        return res


@dataclass
class Branch:
    name: str
    address: str
    telephone: str
    email: str
    manager: str

    def sql_exe(self) -> str:
        res = f"""
INSERT INTO Superhero(
        name,
        address,
        telephone,
        email,
        manager
    )
VALUES(
        "{self.name}",
        "{self.address}",
        "{self.telephone}",
        "{self.email}",
        "{self.manager}"
    );
        """
        return res


@dataclass
class Item:
    name: str
    price: str
    weight: str
    department: str
    supplier: str

    def sql_exe(self) -> str:
        res = f"""
INSERT INTO Superhero(
        name,
        price,
        weight,
        department,
        supplier
    )
VALUES(
        "{self.name}",
        "{self.price}",
        "{self.weight}",
        "{self.department}",
        "{self.supplier}"
    );
        """
        return res


superheroes: dict[int, Superhero] = {
    1: Superhero(
        "Captain Inner Mongolia",
        "Mongolia Center 101, Building M9",
        "Cris",
        "170-4351-2677",
        "mongolia@gmail.com",
        "2005-04-08",
        "Seeing across grasslands.",
    ),
    2: Superhero(
        "The Amazing Cockroach Man",
        "Underground Kitchen D4 201",
        "Frank",
        "114-1519-4476",
        "cm@gmail.com",
        "2004-01-01",
        "Scuttling around rubbish bins.",
    ),
    3: Superhero(
        "Soup Man",
        "BWYA",
        "Mr. Ambler",
        "156-0006-6720",
        "Ambler@gmail.com",
        "2022-01-22",
        "Slurping noodles.",
    ),
    4: Superhero(
        "The Incredible Sulk",
        "Beijing Superbathroom",
        "Antao",
        "186-1072-7130",
        "1801107002@wya.top",
        "2022-10-26",
        "Sulking over predicted grades.",
    ),
    5: Superhero(
        "Batty Girl",
        "Wanderful Land, Utopia",
        "Eric",
        "157-1125-6522",
        "ericshayilin@gmail.com",
        "2005-02-16",
        "Saying inappropriate things.",
    ),
    6: Superhero(
        "Blunder Woman",
        "Crazy Land",
        "Franklin",
        "173-1023-0073",
        "blunder@gmail.com",
        "2005-01-21",
        "Stubbing toes.",
    ),
    7: Superhero(
        "Copper Woman",
        "Mineral Avenue",
        "Charles",
        "150-7891-7871",
        "copperman@who.com",
        "2004-11-15",
        "Conducting electricity.",
    ),
    8: Superhero(
        "Splash",
        "Atom Park Building 7 Room203",
        "Rain",
        "175-3871-1292",
        "splash@who.com",
        "2021-05-13",
        "Having quick showers.",
    ),
}

branches: dict[int, Branch] = {
    1: Branch(
        "Wang Fujing",
        "Beijing City, Wang Fujing Road, Room 101",
        "312-4116-7214",
        "WF@gamil.com",
        "Ms. Guan",
    ),
    2: Branch(
        "Atlantis",
        "Pacific Ocean, Area B, Level 3, Room 41",
        "100-4444-3333",
        "atlantis@gmail.com",
        "Mr. Haysom",
    ),
    3: Branch(
        "Online Taobao",
        "Virtual World",
        "167-7584-3211",
        "taobao@online.com",
        "Ms.Sandy",
    ),
    4: Branch(
        "Parallel Universe",
        "Universe of Parallel Office, Room 8",
        "000-0000-0000",
        "111111@wya.top",
        "Mr. Hugo",
    ),
    5: Branch(
        "Antarctica",
        "Earth No.1",
        "173-1023-0073",
        "ice@gmail.com",
        "Ms. Sophie",
    ),
    6: Branch(
        "Gotham City",
        "Earth No.2 Next to BWYA",
        "114-5141-9198",
        "bat@paet.com",
        "Mr. Ambler",
    ),
    7: Branch(
        "Moon Base",
        "Moontartica",
        "139-1670-2342",
        "gTienc_morn@moon.edu",
        "Mr. K",
    ),
    8: Branch(
        "North Pole",
        "1 North Pole Avenue",
        "170-1919-9191",
        "Horthpale@maile.com",
        "Ms. Chen",
    ),
}

items: dict[int, Item] = {
    1: Item(
        "Criminal Justice Monthly",
        "$ 1.00",
        "0.001 kg",
        "Criminal",
        "IKEA",
    ),
    2: Item(
        "Ray Gun Ammo",
        "$ 1,800,000,000,000.00",
        "1,000,000 kg",
        "Military",
        "BWYA",
    ),
    3: Item(
        "Tin Foil Hat",
        "$ 50.00",
        "0.001 kg",
        "Accessories",
        "Metal Inc",
    ),
    4: Item(
        "Cape & Underpants Combination",
        "$ 25.00",
        "0.2 kg",
        "Clothing",
        "Franklin United",
    ),
    5: Item(
        "Plaster of Paris Arm Cast",
        "$ 12.90",
        "3 kg",
        "Health",
        "J & J Health",
    ),
    6: Item(
        "Toilet Paper",
        "$ 0.99",
        "2.5 g",
        "Toilet Treats",
        "Toilet-Hero",
    ),
    7: Item(
        "Cryptonite",
        "$ 90,000.00",
        "10 kg",
        "Weaponry",
        "Luther Limited",
    ),
    8: Item(
        "Energy Bars",
        "$ 2.00",
        "0.01 kg",
        "Food",
        "Sodexo",
    ),
}
