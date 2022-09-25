import pythonjsonlogger
from mdl.person import Person as Per
from rut_chile import rut_chile
from datetime import datetime
import json
# TODO a lot and more of a lot a things


def ask_data():
    print("Please write the following data")
    print("Name: ")
    nm = input().strip()
    print("Last Name: ")
    lnm = input().strip()
    print("Sex: ")
    sx = input().strip()
    print("Id: ")
    d = input().strip()
    print("Day of birthday: ")
    bd = input().strip()
    print("Month of birthday: ")
    bm = input().strip()
    print("Year of birthday: ")
    by = input().strip()
    return Per.create_person(nm, lnm, d, bd, bm, by, sx)


"""
original_out = sys.stdout
    with open("src/Person.txt", "a") as f:
        sys.stdout = f
        mister.print_person()
        sys.stdout = original_out
ale = ask_data()
ale.print_person()
ale.write_person_file()
x = datetime.datetime.now()
n = datetime.datetime(3022, 12, 25)
print(n.year)
print(n.strftime("on %A %d of %B on the year %Y"))
ale = ask_data()
ale.print_json_person()
"""

