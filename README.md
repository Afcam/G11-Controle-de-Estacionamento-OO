# G11-Controle-de-Estacionamento-OO
## TRABALHO PRÁTICO DE OO - CONTROLE DE ESTACINAMENTO

    Grupo: 11
    Nome: Arthur Faria Campos  Matricula: 16/0024242

### Diagrama de Classes

Aqui estão as principais classes do nosso Sistema de Estacionamento:

* **Hub:** Interface de texto para o sistema.
* **ParkingLot:** A parte central da organização para a qual este software foi projetado.
* **Account:** Conta dos clientes mensalistas .
* **Parking Ticket** Esta classe incluirá um bilhete de estacionamento. Os clientes irão tirar um
  tíquete ao entrar no estacionamento.
* **Vehicle:** Os cadastros de cada veículos que ficarão estacionados nas vagas.
* **Park Rate:** Esta classe manterá o controle das taxas de estacionamento por
  hora, dia e noite.
<p align="center">
    <img src="/media/estacionamento_UML.png" alt="Parking Lot UML">
    <br />
    UML do Estacionamento
</p>

<!-- ### Uso de caso

Aqui estão os principais atores em nosso sistema:

* **Admin:** Principalmente responsável por adicionar e modificar estacionamento, aumentar/diminuir
  vagas, adicionar/remover atendentes de estacionamento, etc.
* **Cliente** Todos os clientes podem obter um tíquete de estacionamento e pagar por ele.
* **Atendente de estacionamento** Os atendentes de estacionamento podem fazer todas as atividades em
  nome do cliente e podem receber dinheiro para o pagamento do tíquete.


Aqui estão os principais casos de uso para estacionamento:

* **Adicionar / Remover / Editar uma vaga de estacionamento:** Para adicionar, remover ou modificar
  uma vaga de estacionamento.
* **Adicionar / Remover um atendente de estacionamento:** Para adicionar ou remover um atendente de
  estacionamento do sistema.
* **Gerar o tíquete:** Para fornecer aos clientes um novo tíquete de estacionamento ao entrar no
  estacionamento.
* **Pagar o tíquete:** Para digitalizar um tíquete para descobrir a taxa total.
* **Pagamento com cartão de crédito:** Para pagar com cartão de crédito.
* **Pagamento à vista:** Para pagar em dinheiro.
* **Adicionar / modificar taxa de estacionamento:** Para permitir que o administrador adicione ou
  modifique a taxa de estacionamento por hora. -->

### Code

A seguir está a estrutura de código básico para o nosso sistema de estacionamento:

**Enums e Data Types:** Aqui estão os tipos comuns  necessários para o codigo:

```python
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

```

**ParkingLot:** Sistema do estacionamento

```python
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
```


**Vehicle:** Classe dos dados de veiculos.

```python
# vehicle.py
from common import  *


class Vehicle:
    def __init__(self, plate_number: str, make: str, model: str, person: Person = None):
        self.__make = make
        self.__model = model
        self.__plate_number = plate_number
        self.__person = person

    def person(self):
        return self.__person

    def plate_number(self):
        return self.__plate_number

    def info(self):
        return self.__make, self.__model, self.__plate_number

    def assign_person(self, person):
        self.__person = person

    def remove_person(self, person):
        if self.__person == person:
            self.__person = None
        else:
            raise Exception("Sorry, not the correct owner")

```

**ParkingRate:** Formas de cobrança

```python
# parking_rate.py
# parking_rate.py
# from .common import *


class ParkingRate:
    def __init__(self, rate=0.5):
        self.rate = rate

    def payment(self, time):
        amount = time * self.rate
        return amount


class FracParkingRate(ParkingRate):
    def __init__(self, rate=0.5, deduction=1.0):
        super().__init__(rate)
        self.deduction = deduction

    def payment(self, time):
        amount = super().payment(time) - (time//15)*1.0
        return amount


class HourParkingRate(FracParkingRate):
    def __init__(self, rate=0.5, frac_deduction=1.0, hour_deduction=1.0):
        super().__init__(rate, frac_deduction)
        self.hour_deduction = hour_deduction

    def payment(self, time):
        amount = super().payment(time) - (time//60)*1.0
        return amount


class DailyParkingRate(HourParkingRate):
    def __init__(self, rate=0.5, fee=110.0,daily_hour=9):
        super().__init__(rate)
        self.fee = fee
        self.daily_hour = daily_hour

    def payment(self, time):
        if time >=self.daily_hour*60:
            self.rate= 0.2
        else:
            self.rae= 0.5

        daily = time//(self.daily_hour*60)
        amount = daily*self.fee + super().payment(time%(self.daily_hour*60))
        return amount


class NightParkingRate(DailyParkingRate):
    def __init__(self, rate=0.5, frac_deduction=1.0, hour_deduction=1.0, fee=30.0):
        super().__init__(rate, frac_deduction, hour_deduction)
        self.fee = fee

    def payment(self, days,time):
        amount = self.fee*days + super().payment(time)
        return amount


class MonthlyParkingRate():
    def __init__(self, fee=500.0):
        self.fee = fee

    def payment(self, time: None):
        amount = self.fee
        return amount


```



**Hub:** Construção da interface grafica para utilização do sistema.

```python
# main.py
#!/usr/bin/env python3
from datetime import date, datetime
import os
from parking_lot import ParkingLot

from common import *


def line(tam=42):
    return '-' * tam


def header(txt):
    print("\n")
    print(line())
    print(txt.center(42))
    print(line())


def read_int(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError,TypeError):
            print('\033[31mERRO: digite um número inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mNão digitou número.\033[m')
            return 0
        else:
            return n


def menu(msg,menu_list):
    header(msg)
    c=1
    for item in menu_list:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(line())
    opc = read_int('\033[32mSua Opção: \033[m')
    return opc


def getAddress():
    # print("\n-- Adress\r\n")
    country = input("Pais: ")
    state = input("Estado: ")
    city = input("Cidade: ")
    street_address = input("Rua: ")
    zip_code = input("CEP: ")

    address = Address(street_address, city, state, zip_code, country)
    return address


class Hub:
    def __init__(self, name:None):
        self.parkinglot = ParkingLot(name)



    def main(self):
        while True:
            op = menu(f'ESTACIONAMENTO {self.parkinglot.name()}',['Cadastrar Mensalista', 'Cadastrar Veiculo', 'Gerar Ticket', 'Pagar Ticket','Sair do sistema'])
            if op == 1:
                self.cadastro_mensalista()
            elif op == 2:
                self.cadastro_veiculo()
            elif op == 3:
                self.GerarTicket()
            elif op == 4:
                self.PagarTicket()
            elif op == 5:
                print("Saindo do sistema... Até logo!")
                break
            else:
                print('ERRO! Digite uma opção válida')


    def cadastro_mensalista(self):
        loop = True
        while loop:
            header("CADASTRO DE MENSALISTA")
            name = input("Nome Completo: ")
            license_number = input("CNH: ")
            address = getAddress()
            phone = input("Numero de Celular: ")
            landline = input("Telefone Fixo: ")

            print(f'\n\nNome: {name} \t CNH: {license_number}')
            print(f'Telefone: {phone} \t Telefone Fixo: {landline}')
            print(f'Enereço:{address.info()}\n')

            print('Os Dados estão corretos?')
            for idx, item in enumerate(['Sair', 'Sim', 'Não']):
                print(f'{idx}\033[m-\033[34m{item}\033[m',end='\t')
            while True:
                op = read_int('\n\033[32mSua Opção: \033[m')
                if op == 1:
                    self.parkinglot.new_account(name, address, phone, license_number, landline)
                    print(f'\nUsuário \033[33m{name}\033[m cadastrado com \033[32msucesso\033[m.')
                    loop = False
                    break
                elif op == 2:
                    break
                elif op == 0:
                    loop = False
                    break
                else:
                    print('ERRO! Digite uma opção válida')


    def cadastro_veiculo(self,plate_number=None):
        while True:
            header("CADASTRO DE VEICULO")
            make = input("Fabricante: ")
            model = input("Modelo: ")
            if plate_number==None:
                plate_number = input("Placa: ")
            person_name = input("Proprietário: ")
            if person_name!=None:
                person = self.parkinglot.check_person(person_name)
                if person == None:
                    print("Prorietario não encontrado")
            else:
                person = None

            print(f'\n\nModelo: {make} \t Fabricante: {model}')
            print(f'Placa: {plate_number} ')

            print('Os Dados estão corretos?')
            for idx, item in enumerate(['Sair', 'Sim', 'Não']):
                print(f'{idx}\033[m-\033[34m{item}\033[m',end='\t')
            while True:
                op = read_int('\n\033[32mSua Opção: \033[m')
                if op == 1:
                    new =  self.parkinglot.new_vehicle( plate_number, make, model, person)
                    print(f'\nVeiculo \033[33m{plate_number}\033[m cadastrado com \033[32msucesso\033[m.')
                    return new
                    break
                elif op == 2:
                    break
                elif op == 0:
                    return None
                else:
                    print('ERRO! Digite uma opção válida')

    def GerarTicket(self):
        header("Gerar Ticket")
        plate_number = input("Placa do Veiculo: ")

        veh = self.parkinglot.check_vehicle(plate_number)
        if veh == None:
            veh = self.cadastro_veiculo(plate_number)

        ticket = self.parkinglot.new_ticket(veh)
        dt_string = ticket.entry_time.strftime("%d/%m/%Y %H:%M:%S")
        print(f'\nTicket cadastrado em\033[33m',dt_string, '\033[mcom \033[32msucesso\033[m.')


    def PagarTicket(self):
        header("Pagar Ticket")
        plate_number = input("Placa do Veiculo: ")


        ticket = self.parkinglot.get_ticket(plate_number)
        if ticket == None:
            raise Exception('TicketNãoExiste')
        else:
            amount = self.parkinglot.pay_ticket(ticket)

        print(f'\nTOTAL:\033[33m{amount}\033[m.')


if __name__ == "__main__":
    header("Bem Vindo")
    name = input('Nome do Estacionamento: ')
    Program = Hub(name)
    Program.main()


```