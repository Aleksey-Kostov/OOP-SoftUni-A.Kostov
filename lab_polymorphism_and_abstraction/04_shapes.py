from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def __init__(self, height, width):
        self.__height = height
        self.__width = width
