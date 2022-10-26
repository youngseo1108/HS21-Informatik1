from abc import ABC, abstractmethod


class GeometricObject(ABC):
    def __init__(self, color, filled):
        self.__color = color # str
        self.__filled = filled # bool

    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color
        return self.__color

    def get_filled(self):
        return self.__filled
    
    def set_filled(self, filled):
        self.__filled = filled
        return self.__filled
    
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_volume(self):
        pass