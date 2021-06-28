from datetime import datetime
from random import randint


class Animal:
    dict = {'Bulldog': 12,
            'Chihuahua': 20,
            'Pinscher': 15}
    actual_year = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, name, age, race, alive=True):
        self.name = name
        self.age = age
        self.race = race
        self.alive = alive

    @classmethod
    def born_year_method(cls, name, race, born_year):
        age = cls.actual_year - born_year
        alive = True

        try:
            try:
                if age == 1:
                    print(f'{name} has {age} years old')
                elif cls.dict[race] >= age > 1:
                    print(f'{name} has {age} years old')
                elif age > cls.dict[race]:
                    print(f'{name} would have {age} years old'
                          f', but it\'s nor here with us anymore')
                    alive = False
                elif born_year >= cls.actual_year:
                    print(f'{name} has not born yet')
            except KeyError:
                print(f'We dont have \'{race}\' in our Database')
        except ValueError:
            print('Invalid Age!')
        return cls(name, age, race, alive)

    @staticmethod
    def id_animal_generator():
        id_animal = randint(100000, 199999)
        return id_animal
