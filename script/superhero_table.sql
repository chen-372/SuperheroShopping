DROP TABLE Superhero;
CREATE TABLE Superhero(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    true_identity TEXT NOT NULL,
    telephone TEXT NOT NULL,
    email TEXT NOT NULL,
    date_of_birth TEXT NOT NULL,
    super_power TEXT NOT NULL
);