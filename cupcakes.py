from abc import ABC, abstractmethod
from asyncore import read
import csv
from pprint import pprint

class Cupcake(ABC):
    size = 'Regular'
    def __init__(self, name, price, flavor, frosting, sprinkles, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = sprinkles
        self.filling = filling
        # def __repr__(self): 
        #     return  (self.size, self.name) 
    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod 

    def calculate_price(self, quantity):
        return quantity * self.price

class Mini(Cupcake):
    size = 'Mini'
    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []
        

    def calculate_price(self, quantity):
        return quantity * self.price

class Large(Cupcake):
    size = 'Large'
    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

    def calculate_price(self, quantity):
        return quantity * self.price
        
class Regular(Cupcake):
    size = 'Regular'
    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

    def calculate_price(self, quantity):
        return quantity * self.price
        
def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile) 
        for row in reader:
            pprint(row)


def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ['size', 'name', 'price', 'flavor', 'frosting', 'sprinkles', 'filling']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})

def add_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if hasattr(cupcake, "filling"):
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
        else:
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})

def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)


cupcake1 = Regular("Stars and Stripes", 2.99, "Vanilla", "Vanilla")
cupcake1.add_sprinkles("Red", "White", "Blue")
cupcake2 = Mini("Oreo", .99, "Chocolate", "Cookies and Cream")
cupcake2.add_sprinkles("Oreo pieces")
cupcake3 = Large("Red Velvet", 3.99, "Red Velvet", "Cream Cheese")

cupcake_list = [
    cupcake1,
    cupcake2,
    cupcake3
]

add_cupcake('newCupcakeList.csv', Regular('Black and Yellow' , 2.49 , 'Chocolate' , "Vanilla"))

# write_new_csv('newCupcakeList.csv', cupcake_list)
# read_csv('starter/sample.csv')

# my_cupcake_mini = Mini('Chocolate Chip', 2.99, 'Chocolate', 'White Swirl',['Oreo Crumbs'])
# print(my_cupcake_mini.name)
# print(my_cupcake_mini.price)
# print(my_cupcake_mini.size)

# my_cupcake = Cupcake('Red Velvet', 4.98, 'Red Velvet', 'Cream Cheese', [], True) 


# my_cupcake.frosting = 'Chocolate'
# my_cupcake.filling = 'Chocolate'
# my_cupcake.name = 'Double Chocolate Red Velvet'
# my_cupcake.is_miniature = False


# my_cupcake.add_sprinkles('Oreo crumbs', 'Chocolate', 'Vanilla')
# print(my_cupcake.sprinkles)
# print([my_cupcake])
# print(my_cupcake.name)
# print(my_cupcake.is_miniature)