#!/usr/bin/env python3
from datetime import date, datetime
import os
# from .parking_lot import *
# from .common import *
# from .parking_rate import *
# from .vehicle import *
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

