#!/usr/bin/env python3
import os
# from .parking_lot import *
# from .common import *
# from .parking_rate import *
# from .vehicle import *
from src.parking_lot import ParkingLot

from src.common import *


def line(tam=42):
    return '-' * tam


def header(txt):
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
    country = input("Pais: ")
    state = input("Estado: ")
    city = input("Cidade: ")
    street_address = input("Rua: ")
    zip_code = input("CEP: ")

    address = Address(street_address, city, state, zip_code, country)
    return address


def main():
    header("Bem Vindo")
    name = input('Nome do Estacionamento: ')
    parkinglot = ParkingLot(name)

    while True:
        op = menu(f'ESTACIONAMENTO {name}',['Cadastrar Mensalista', 'Cadastrar Veiculo', 'Gerar Ticket', 'Pagar Ticket','Sair do sistema'])
        if op == 1:
            header("CADASTRO DE MENSALISTA")
            name = input("Nome Completo: ")
            license_number = input("CNH: ")
            address = getAddress()
            phone = input("Numero de Celular: ")
            landline = input("Telefone Fixo: ")

            parkinglot.new_account(name, address, phone, license_number, landline)
            parkinglot.list_accounts()
        elif op == 2:
            header("CADASTRO DE VEICULO")
        elif op == 3:
            header("GERAR TICKET")
        elif op == 4:
            header("PAGAR TICKET")
        elif op == 5:
            print("Saindo do sistema... Até logo!")
            break
        else:
            print('ERRO! Digite uma opção válida')

if __name__ == "__main__":
    main()

