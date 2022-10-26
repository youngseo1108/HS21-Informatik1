# TASK 4. Car Types
'''
CombustionCars are initiated with the gas_capacity in liters and gas_per_100km 
that describes the fuel consumption. 

c = CombustionCar(40.0, 8.0)
c.get_remaining_range() # 500
c.drive(25.0)
c.get_gas_tank_status() # (38.0, 40.0)
c.drive(1000.0) # fuel is depleted, Warning raised
'''
from car import Car

def assertPositiveFloat(n):
    if type(n) != float or n < 0:
        raise Warning('Invalid input.')

class CombustionCar(Car):

    def __init__(self, gas_capacity, gas_per_100km):
        assertPositiveFloat(gas_capacity)
        assertPositiveFloat(gas_per_100km)
        self.__gas_max = gas_capacity
        self.__gas_current = gas_capacity
        self.__gas_per_100km = gas_per_100km

    def fuel(self, f):
        # The car can be refueled using fuel, 
        # which adds f liters of fuel to the gas tank. 
        # The method should raise a Warning, 
        # if the gas tank gets overfilled.
        assertPositiveFloat(f)
        if self.__gas_current + f > self.__gas_max:
            raise Warning('Oil has overfilled.')
        self.__gas_current += f

    def get_gas_tank_status(self):
        # returns the current gas tank capacity c & the maximum capacity c_max 
        # as a tuple (c, c_max). 
        # It must always be that 0 <= c <= c_max.
        c = self.__gas_current
        c_max = self.__gas_max
        return (c, c_max)

    def get_remaining_range(self):
        return 100*self.__gas_current / self.__gas_per_100km

    def drive(self, dist):
        # remove the correct amount of gas from the gas tank 
        # and it should raise a Warning, 
        # if the gas tank is fully depleted through driving. 
        assertPositiveFloat(dist)
        dist /= 100
        consumption = dist * self.__gas_per_100km
        if self.__gas_current < consumption:
            self.__gas_current = 0.0
            raise Warning('Gas tank is empty.')
        self.__gas_current -= consumption