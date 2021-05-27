# common.py
from enum import Enum
from datetime import *
import math


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

    def info(self):
        return self.__country, self.__city, self.__state, self.__street_address, self.__zip_code


class Person:
    def __init__(self, name, address, phone, license_number, landline=None):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__landline = landline
        self.__license_number = license_number

    def info(self):
        return self.__name, self.__address, self.__phone, self.__landline, self.__license_number

    def name(self):
        return  self.__name



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


class Ticket():
    def __init__(self, entry_time, vehicle, status=ParkingTicketStatus.ACTIVE):
        self.AM6 = entry_time.replace(hour=6, minute=0, second=0, microsecond=0)
        self.PM20 = entry_time.replace(hour=20, minute=0, second=0, microsecond=0)
        if self.AM6.time() >= entry_time.time() >= self.PM20.time() :
            raise Exception('EstacionamentoFechadoException')
        else:
            self.__status = status
            self.entry_time = entry_time
            self.exit_time = entry_time
            self.vehicle = vehicle

    def status(self):
        return self.__status

    def entry_time(sel):
        return self.entry_time.time()

    def paid(self):
        self.__status = ParkingTicketStatus.PAID

    def set_exit_time(self,exit_time):
        if self.AM6.time() >= exit_time.time() >= self.PM20.time() :
            raise Exception('EstacionamentoFechadoException')
        else:
            self.exit_time = exit_time

    def elapsed_time(self):
        diff =  self.exit_time -  self.entry_time
        # minutes = int(diff.total_seconds()/60)
        dates =  AM6.date() -  PM8.date()
        days = dates.days
        minutes = int(diff.total_seconds()/60) - days*10*60
        return days, minutes

if __name__ == "__main__":
    now = datetime.now()
    # tick = Ticket(now,None)
    AM6 = now.replace(day= 18,hour=6, minute=0, second=0, microsecond=0)
    PM8 = now.replace(day= 17,hour=20, minute=0, second=0, microsecond=0)

