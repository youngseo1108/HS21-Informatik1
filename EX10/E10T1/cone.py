'''
1. Your task is to build the object-orietened hierarchy as per the UML diagram above.
2. You should implement Cone,Cube and Cylinder classes.
3. For the sake of simpilicty you are not required to implement setters 
for specialized geometric classes Cone,Cube and Cylinder. 
You should only implement getters for their instance attributes.
4. Each special geometric object has it's unique formula to calculate area and volume. 
You need to apply these formulas in the appropriate functions. You can find the formulas in the table below.
5. get_area and get_volume functions should return float with rounded to 2 decimal points. 
i.e. Calculated area 19.32494 should be returned as 19.32
6. You should take PI as 3.14 .
'''
from public.geometric_object import GeometricObject


class Cone(GeometricObject):
    def __init__(self, radius, vertical_height, slant_height, color, filled):
        super().__init__(color, filled)
        self.__radius = radius
        self.__vertical_height = vertical_height
        self.__slant_height = slant_height
        self.__PI = 3.14

    def get_radius(self):
        return self.__radius

    def get_vertical_height(self):
        return self.__vertical_height
    
    def get_slant_height(self):
        return self.__slant_height

    def get_area(self):
        area = self.__PI*(self.__radius**2) + self.__PI*self.__radius*self.__slant_height
        return round(area, 2)

    def get_volume(self):
        volume = (1/3)*self.__PI*(self.__radius**2)*self.__vertical_height
        return round(volume, 2)



# For the Cone object initiated with Cone(4,10,10.77,red,True) 
# expected volume return was 167.47 but 180.36 is found

volume = (1/3)*3.14*(4**2)*10
print(volume)