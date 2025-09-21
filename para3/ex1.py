class Human:
    def __init__(self, name):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passenger = []

    def add_passenger(self, human):
        self.passenger.append(human)

    def print_passenger(self):
        if self.passenger != []:
            print(f"Names {self.brand} passenger")
            for person in self.passenger:
                print(person.name)
        else:
            print(f"{self.brand} are no passenger")


persona1 = Human("Nick")
persona2 = Human("Lisa")
persona3 = Human("Vasya")
avto = Auto("Mercedes")
avto.add_passenger(persona1)
avto.add_passenger(persona2)
avto.print_passenger()
avto.add_passenger(persona3)
avto.print_passenger()
