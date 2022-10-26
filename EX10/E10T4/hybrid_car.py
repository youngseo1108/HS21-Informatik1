'''
Finally, HybridCar inherits all properties and functionalities of the other two car types and, 
as such, needs all parameters for the initialization. 
The two methods switch_to_combustion and switch_to_electric can be used to change the operation mode. 
Should the car run out of fuel or battery during a tour, it should automatically switch the mode. 
If both modes are fully depleted, the car should raise a Warning. 
HybridCar inherits two conflicting definitions of the methods get_remaining_range and drive, 
adapt the implementations to make them work. The usage of a hybrid car is similar to the previous examples:

h = HybridCar(40.0, 8.0, 25.0, 500.0)
h.switch_to_combustion()
h.drive(600.0) # depletes fuel, auto-switch
h.get_gas_tank_status() # (0.0, 40.0)
h.get_battery_status() # (20.0, 25.0)
'''

from combustion_car import CombustionCar
from electric_car import ElectricCar

def assertPositiveFloat(n):
    if type(n) != float or n < 0:
        raise Warning('Invalid input.')

class HybridCar(CombustionCar, ElectricCar):

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
        CombustionCar.__init__(self, gas_capacity, gas_per_100km)
        ElectricCar.__init__(self, battery_size, battery_range_km)
        self.__use_battery = True

    def switch_to_combustion(self):
        self.__use_battery = False

    def switch_to_electric(self):
        self.__use_battery = True

    def get_remaining_range(self):
        c = CombustionCar.get_remaining_range(self)
        e = ElectricCar.get_remaining_range(self)
        return c + e

    def drive(self, dist):
        assertPositiveFloat(dist)
        if dist > self.get_remaining_range():
            self.__gas_current = 0
            self.__battery_current = 0
            raise Warning('Lack of oil and battery.')
        if self.__use_battery:
            e = ElectricCar.get_remaining_range(self)
            if dist > e:
                ElectricCar.drive(self, e)
                self.switch_to_combustion()
                CombustionCar.drive(self, dist - e)
            else:
                ElectricCar.drive(self, dist)
        else:
            c = CombustionCar.get_remaining_range(self)
            if dist > c:
                CombustionCar.drive(self, c)
                self.switch_to_electric()
                ElectricCar.drive(self, dist - c)
            else:
                CombustionCar.drive(self, dist)