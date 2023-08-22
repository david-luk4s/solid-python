from abc import ABC, abstractmethod

class Area(ABC):

    @classmethod
    @abstractmethod
    def get_area():
        """return area"""


class Quadrado(Area):
    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def get_area(self):
        return self.size * self.size


class Retangulo(Area):
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_width(self):
        return self.width
    
    def get_height(self):
        self.height

    def get_area(self):
        return self.width * self.height

if __name__ == '__main__':
    quad = Quadrado()
    quad.set_size(4)
    print(quad.get_area())

    ret = Retangulo()
    ret.set_height(4)
    ret.set_width(4)
    print(ret.get_area())
