from sqlite3 import connect
from data import superheroes, items, branches

with connect("test.sqlite3") as connection:
    for dicts in [superheroes, items, branches]:
        for n in dicts.values():
            exe = n.sql_exe()
            print(exe)
            cursor = connection.execute(exe)
