from abc import ABC
from enum import Enum

# from src.vehicle import Vehicle


class ParkingTicketStatus(Enum):
    ACTIVE, PAID, LOST = 1, 2, 3


class Address:
    def __init__(self, street:str, city:str, state:str, zip_code:str, country:str):
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country


class Person:
    def __init__(self, name: str, address: Address, phone: str, license_number: str, landline: str=None):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__landline = landline
        self.__license_number = license_number


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


class Account(Person):
    def __init__(self, name: str, address: Address, phone: str, license_number: str, landline: str = None):
        super().__init__(name, address, phone, license_number, landline)
        self.__cars = []

    def assign_vehicle(self, vehicle:Vehicle):
        # Check if not already added
        if vehicle in self.__cars:
            print("Yes, 'S Eductation' found in List : ", self.__cars)
        else:
            self.__cars.append(vehicle)

    def remove_vehicle(self, vehicle:Vehicle):
        self.__cars.remove(vehicle)

    def list_vehicle(self):
        for car in self.__cars:
            print(car.plate_number)


class ParkingLot:
    # singleton ParkingLot to ensure only one object of ParkingLot in the system
    # instance = None
    #
    # class __OnlyOne:
    #     def __init__(self, name, address):
    #         self.__name = name
    #         self.__address = address
    #         # self.__parking_rate = ParkingRate()
    #
    #         # all active parking tickets, identified by their ticket_number
    #         self.__active_tickets = {}
    #
    #         self.__vehicles = []
    #         self.__accounts = []

            # self.__lock = threading.Lock()

    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        # self.__parking_rate = ParkingRate()

        # all active parking tickets, identified by their ticket_number
        self.__active_tickets = {}

        self.__vehicles = []
        self.__accounts = []
        #
        # if not ParkingLot.instance:
        #     ParkingLot.instance = ParkingLot.__OnlyOne(name, address)
        # else:
        #     ParkingLot.instance.__name = name
        #     ParkingLot.instance.__address = address

    # def __getattr__(self, name):
    #     return getattr(self.instance, name)

    def get_new_parking_ticket(self, vehicle):
        pass

    def new_account(self, name, address, phone, license_number, landline):
        new = Account(name, address, phone, license_number, landline)
        self.__accounts.append(new)

    def list_accounts(self):
        for acc in self.__accounts:
            print(acc)


if __name__ == "__main__":
    Estacionamento = ParkingLot('Brasilia', 'FGA')
    name = "Arthur"
    address = "SQN"
    phone = "61998779966"
    license_number = "OHasdhaAJ"
    landline = None
    Estacionamento.new_account(name, address, phone, license_number, landline)
    Estacionamento.list_accounts()
    print("Oi")

