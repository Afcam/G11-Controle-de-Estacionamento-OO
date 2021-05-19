# parking_lot.py
from src.parking_rate import ParkingRate
from src.common import *


class ParkingLot:
    def __init__(self, name):
        self.__name = name
        self.__parking_rate = ParkingRate()

        self.__vehicles = {}
        self.__accounts = []
        self.__active_tickets = {}

    # def __getattr__(self, name):
    #     return getattr(self.instance, name)

    # def get_new_parking_ticket(self, vehicle):
    # synchronizing to allow multiple entrances panels to issue a new
    # parking ticket without interfering with each other
    #     self.__lock.acquire()
    #     ticket = ParkingTicket()
    #     vehicle.assign_ticket(ticket)
    #     ticket.save_in_DB()
    #     # if the ticket is successfully saved in the database, we can increment the parking spot count
    #     self.__increment_spot_count(vehicle.get_type())
    #     self.__active_tickets.put(ticket.get_ticket_number(), ticket)
    #     self.__lock.release()
    #     return ticket

    def new_account(self, name, address, phone, license_number, landline):
        new = Account(name, address, phone, license_number, landline)
        self.__accounts.append(new)

    def list_accounts(self):
        for acc in self.__accounts:
            print(acc.info()[0])


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

