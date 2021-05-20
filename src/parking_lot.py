# parking_lot.py
from parking_rate import *
from vehicle import *
from common import *
from datetime import *


class ParkingLot:
    def __init__(self, name):
        self.__name = name
        self.__parking_rate = 0.5

        self.__vehicles = []
        self.__accounts = []
        self.__active_tickets = []

    def name(self):
        return self.__name

    def new_vehicle(self, plate_number, make, model, person):
        for item in self.__vehicles:
            if item.plate_number() == plate_number:
                return item

        new = Vehicle(plate_number, make, model, person)
        self.__vehicles.append(new)
        return new


    def new_account(self, name, address, phone, license_number, landline):
        new = Account(name, address, phone, license_number, landline)
        self.__accounts.append(new)

    def list_accounts(self):
        for acc in self.__accounts:
            print(f'\n{acc.info()[0]}')

    def list_vehicles(self):
        for acc in self.__vehicles:
            print(f'\n{acc.info()[0]}')

    def check_person(self, person_name):
        for acc in self.__accounts:
            if acc.name() == person_name:
                return acc
        return None

    def check_vehicle(self, plate_number):
        for item in self.__vehicles:
            if item.plate_number() == plate_number:
                return item
        return None

    def get_ticket(self, plate_number):
        for tic in self.__active_tickets:
            if tic.vehicle.plate_number() == plate_number:
                return tic
        return None

    def new_ticket(self, vehicle):
        now = datetime.now()

        new_ticket = Ticket(now, vehicle)
        self.__active_tickets.append(new_ticket)
        return new_ticket

    def pay_ticket(self, ticket):
        now = datetime.now()

        ticket.set_exit_time(now)

        days, minutes = ticket.elapsed_time()

        if ticket.vehicle.person() !=None:
            rate = MonthlyParkingRate()
        elif days > 0:
            rate = NightParkingRate()
            amount = rate.payment(days,minutes)
        else:
            if minutes < 15 :
                rate = ParkingRate()
            elif 15 <= minutes < 9*60:
                rate = FracParkingRate()
            elif 9*60 <= minutes:
                rate = HourParkingRate()
            else:
                rate = DailyParkingRate()

            amount = rate.payment(minutes)

        ticket.paid()
        self.__active_tickets.remove(ticket)

        return amount









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

