'''
ElectricCars are initiated with a battery_size in kilo-watt hours and the range of a fully charged battery in kilometers. 
The battery can be recharged with kwh kilo-watt hours by calling charge. 
Like for CombustionCar, over-charging should raise a Warning. 
Also get_battery_status is very similar to the CombustionCar equivalent 
and should return the current and the maximum capacity in a tuple (c, c_max). 
drive and get_remaining_range need to be implemented as well and should affect/be affected by the battery charge level.
'''

from car import Car

def assertPositiveFloat(n):
    if type(n) != float or n < 0:
        raise Warning('Invalid input.')

class ElectricCar(Car):

    def __init__(self, battery_size, battery_range_km):
        assertPositiveFloat(battery_size)
        assertPositiveFloat(battery_range_km)
        self.__battery_current = battery_size
        self.__battery_max = battery_size
        self.__range = battery_range_km        

    def charge(self, kwh):
        assertPositiveFloat(kwh)
        if kwh + self.__battery_current > self.__battery_max:
            raise Warning('Overcharged.')
        self.__battery_current += kwh

    def get_battery_status(self):
        c = self.__battery_current
        c_max = self.__battery_max
        return (c, c_max)


    def get_remaining_range(self):
        return self.__battery_current / self.__consumption_per_km()

    def drive(self, dist):
        assertPositiveFloat(dist)
        consumption = dist * (self.__battery_max / self.__range)
        if consumption > self.__battery_current:
            self.__battery_current = 0.0
            raise Warning('Battery depleted.')
        self.__battery_current -= consumption