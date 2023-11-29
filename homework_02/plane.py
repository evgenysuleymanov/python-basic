"""
создайте класс `Plane`, наследник `Vehicle`
"""


from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        Vehicle.__init__(self, weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, num):
        if self.max_cargo >= (num + self.cargo):
            self.cargo += num
        else:
            raise CargoOverload(f'Cargo Over Load')

    def remove_all_cargo(self):
        res = self.cargo
        self.cargo = 0
        return res