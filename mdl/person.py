import json
import timeit as tm


class Person:
    def __new__(cls, *args, **kwargs):
        print("Creating a new instance.")
        return super().__new__(cls)

    def __init__(self, p_nam, p_las, p_ide, p_day, p_mon, p_yea, p_sex):
        print("Initializing the new instance.")
        self.name = p_nam
        self.lastName = p_las
        self.identity = p_ide
        self.b_day = p_day
        self.b_month = p_mon
        self.b_year = p_yea
        self.sex = p_sex

    def __repr__(self) -> str:
        return f"{type(self).__name__}(Name = {self.name}, Last Name = {self.lastName}," \
               f" Sex = {self.sex}, ID = {self.identity}," \
               f" Birthday = {self.b_day}/{self.b_month}/{self.b_year})"

    def print_person(self):
        print(self)

    def age_calc(self, c_year, c_month, c_day):
        age = c_year - int(self.b_year)
        if c_month < int(self.b_month) or \
                (c_month == int(self.b_month) and c_day < int(self.b_day)):
            age -= 1
        return age

    def string_person(self):
        print(self)

    def write_person_file(self):
        data_person = "\nName: " + self.name + " " + self.lastName + " Sex: " + self.sex + \
                      " Born in " + self.b_day + "/" + self.b_month + "/" + self.b_year
        data_person = data_person + " is " + str(self.age_calc(2022, 8, 9)) + " years old"
        person_file = open("./src/Person.txt", "a")
        person_file.write(data_person)
        person_file.close()
        print("Person", self.name, "added to the file.")

    def decoration(func):
        def wrap(*args, **kwargs):
            print("Creating person...")
            p = func(*args, **kwargs)
            print("Person created...")
            return p
        return wrap

    @decoration
    def create_person(nm, lnm, d, db, mb, yb, sx):
        return Person(nm, lnm, d, db, mb, yb, sx)

    def create_json_person(self):
        jp = '{ "first name":"%s", "last name":"%s", "sex":"%s", "id":"%s", "birthdate":"%s-%s-%s" }'\
             % (self.name, self.lastName, self.sex, self.identity, self.b_day, self.b_month, self.b_year)
        par = json.loads(jp)
        return par

    def print_json_person(self):
        print(json.dumps(self.create_json_person(), indent=4))
