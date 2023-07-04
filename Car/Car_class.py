# Create Car class
class Car:
    # constructor
    def __init__ (self, model = 2023, make = "Ford Mustang GT", speed=0):
        self.__year_model = model
        self.__make = make
        self.__speed = speed

    # accelerate method add 5 each time it is called
    # brake method decrease 5 each time it is called 
    # get current speed
