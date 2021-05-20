# parking_lot.py
from parking_rate import ParkingRate
from vehicle import *
from common import *
from datetime import *


class ParkingLot:
    def __init__(self, name):
        self.__name = name
        self.__parking_rate = ParkingRate()

        self.__vehicles = []
        self.__accounts = []
        self.__active_tickets = {}

    def name(self):
        return self.__name

    def new_vehicle(self, plate_number, make, model, person):
        exist=False
        for item in self.__vehicles:
            if item.plate_number() == plate_number:
                exist=True
                break

        if not exist:
            new = Vehicle(plate_number, make, model, person)
            self.__accounts.append(new)
            status = True
        else:
            # raise error
            status = False
        return status

    def new_account(self, name, address, phone, license_number, landline):
        new = Account(name, address, phone, license_number, landline)
        self.__accounts.append(new)

    def list_accounts(self):
        for acc in self.__accounts:
            print(f'\n{acc.info()[0]}')

    def list_vehicles(self):
        for acc in self.__vehicles:
            print(f'\n{acc.info()[0]}')


            from datetime import *

    def check_person(self, person_name):
        find = False
        for acc in self.__accounts:
            if acc.name() == person_name:
                exist=True
                break

        if not exist:
            new = Vehicle(plate_number, make, model, person)
            self.__accounts.append(new)
            status = True
        else:
            # raise error
            status = False
        return status


if __name__ == "__main__":
    Estacionamento = ParkingLot('Brasilia')
    name = "Arthur"
    address = "SQN"
    phone = "61998779966"
    license_number = "OHasdhaAJ"
    landline = None
    Estacionamento.new_account(name, address, phone, license_number, landline)
    Estacionamento.new_account(name, address, phone, license_number, landline)
    Estacionamento.new_account("mas", address, phone, license_number, landline)
    Estacionamento.new_account(name, address, phone, license_number, landline)
    Estacionamento.new_account(name, address, phone, license_number, landline)

    Estacionamento.list_accounts()
    print("Oi")

