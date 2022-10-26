'''
DeliveryRestaurantss are initiated with a 
maximum delivery_radius in kilometers. 
These restaurants only provide the method 
is_in_range(distance) which checks whether the delivery distance lies 
within the delivery_radius. 
If it does True must be returned, if not, False must be returned.
'''
from restaurant import Restaurant

class DeliveryRestaurant(Restaurant):

    def __init__(self, name, cuisine_type, delivery_radius, is_open=False):        
        super().__init__(name, cuisine_type, is_open)
        self.__delivery_radius = delivery_radius

    def is_in_range(self, distance):
        if distance <= self.__delivery_radius and distance >= 0:
            return True
        return False