
class Plant:
    def __init__(self,color):
        self.__color = color


    def get_color(self):
        return self.__color

# flower is the subclass to plant
# superclass cannot access methods in the subclass
# subclass can access methods in the superclass
class Flower(Plant):
    def __init__(self,color, petals):
        Plant.__init__(self,color)

        self.__petals = petals

    def get_petals(self):
        return self.__petals
