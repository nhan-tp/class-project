# Create a class Person with attributes
import math


class Person:
    # (name, age, ethnicity, height in inches, hair color)
    def __init__(self, name, age, ethnicity, height_in_inches, hair_color):
        self.name = name
        self.age = age
        self.ethnicity = ethnicity
        self.height_in_inches = height_in_inches
        self.hair_color = hair_color

    # and with functions
    def get_height_str(self):
        inches = self.height_in_inches

        if inches % 12 != 0:
            feet = int(math.floor(inches / 12))
            inches_remain = inches % 12
            return "{}ft {}in".format(feet, inches_remain)
        else:
            feet = int(inches / 12)
            return "{}ft".format(feet)

    def print_all_attributes(self):
        print("Name:{}".format(self.name))
        print("Age:{}".format(self.age))
        print("Ethnicity:{}".format(self.ethnicity))
        print("Height:{}".format(self.get_height_str()))
        print("Hair color: {}".format(self.hair_color))