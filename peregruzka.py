class Building:

    def __init__(self, number_of_floors, building_type):
        self.a = number_of_floors
        self.b = building_type
        self.info()

    def info(self):
        print(f'Количество этажей: {self.a}, тип здания: {self.b}')

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b


a = Building(1, 'Дом')
b = Building(2, 'Дом')

print(a == b)
