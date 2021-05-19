# common.py
from enum import Enum


class ParkingTicketStatus(Enum):
    ACTIVE, PAID, LOST = 1, 2, 3


class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6


class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country


class Person:
    def __init__(self, name, address, phone, license_number, landline=None):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__landline = landline
        self.__license_number = license_number

    def info(self):
        return self.__name, self.__address, self.__phone, self.__landline, self.__license_number



class Account(Person):
    def __init__(self, name, address, phone, license_number, landline = None, status=AccountStatus.ACTIVE):
        super().__init__(name, address, phone, license_number, landline)
        self.__cars = []
        self.__status = status


    def assign_vehicle(self, vehicle):
        # Check if not already added
        if vehicle in self.__cars:
            print("Yes, 'S Eductation' found in List : ", self.__cars)
        else:
            self.__cars.append(vehicle)

    def remove_vehicle(self, vehicle):
        self.__cars.remove(vehicle)

    def list_vehicle(self):
        for car in self.__cars:
            print(car.plate_number)
