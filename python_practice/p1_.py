import numpy as np

# lists

students_list = []


def class_enroll():
    i = 0
    while i < 10:
        print('Enroll yourself: ')
        name = input()

        students_list.append(name)
        i += 1


def class_list():
    print(students_list)


# class_enroll()
# class_list()

class Item:
    list_of_attributes = []

    def __init__(self, name, material, integrity=100):
        self.name = name
        self.material = material
        self.integrity = integrity


class Bag:
    def __init__(self):
        self.items = []

    def add_item(self, new_item):
        self.items.append(new_item)


i_01 = Item('Sword', 'Iron')
i_02 = Item('Mace', 'Bronze')
i_03 = Item('Dagger', 'Mithril', 0)
bag = Bag()

bag.add_item(i_01)

# print(bag.items)

# def found(item):
#     global bag
#     if item.integrity == 0:
#         print(f'The {item.name} is broken')
#         return
#     bag = np.append(bag, item)


# found(i_01)
print(bag)

# def lost():
#
# def conquers():
