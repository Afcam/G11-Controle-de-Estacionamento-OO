# parking_interface.py
from .common import  *


class Vehicle:
    def __init__(self, plate_number: str, make: str, model: str, person: Person = None):
        self.__make = make
        self.__model = model
        self.__plate_number = plate_number
        self.__person = person

    def person(self):
        return self.__person

    def info(self):
        return self.__make, self.__model, self.__plate_number

    def assign_person(self, person):
        self.__person = person

    def remove_person(self, person):
        if self.__person == person:
            self.__person = None
        else:
            raise Exception("Sorry, not the correct owner")