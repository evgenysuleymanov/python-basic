from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=100, fuel=100, fuel_consumption=10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if self.fuel > 0 and self.started is False:
            self.started = True
        elif self.started is True:
            print(f'Started is True')
        else:
            raise LowFuelError(f'Low Fuel')

    def move(self, distance):
        if 0 <= self.fuel <= self.fuel_consumption:
            raise NotEnoughFuel('Not Fuel')
        elif self.fuel < (distance * self.fuel_consumption):
            raise NotEnoughFuel('Not Fuel')
        else:
            self.fuel -= (distance * self.fuel_consumption)