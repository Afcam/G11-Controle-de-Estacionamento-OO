# parking_interface.py
from abc import ABC
from .constants import  *


class Vehicle(ABC):
    def __init__(self, plate_number, make, model):
        self.__make = make
        self.__model = model
        self.__plate_number = plate_number