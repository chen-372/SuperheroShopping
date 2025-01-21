CREATE TABLE Purchase(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    superhero_id INT NOT NULL,
    item_id INT NOT NULL,
    branch_id INT NOT NULL,
    FOREIGN KEY (superhero_id) REFERENCES Superhero(id),
    FOREIGN KEY (item_id) REFERENCES Item(id),
    FOREIGN KEY (branch_id) REFERENCES Branch(id)
);