from geometric_object import GeometricObject


class Cylinder(GeometricObject):
    def __init__(self, radius, height, color, filled):
        super().__init__(color, filled)
        self.__radius = radius
        self.__height = height
        self.__PI = 3.14

    def get_radius(self):
        return self.__radius

    def get_height(self):
        return self.__height

    def get_area(self):
        area = 2*self.__PI*(self.__radius**2) + 2*self.__PI*self.__radius*self.__height
        return round(area, 2)

    def get_volume(self):
        volume = self.__PI*(self.__radius**2)*self.__height
        return round(volume, 2)

# For the cylinder object initiated with cylinder(10,5,red,True) 
# expected area return was 942 but 628.0 is found

area = 2*3.14*(10**2) + 2*3.14*10*5
volume = 3.14*(10**2)*5
print(area)
print(volume)