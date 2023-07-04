# Create Car class
class Car:
    # constructor
    def __init__ (self, year_model = 2023, make = "Ford Mustang GT", speed=0):
        self.__year_model = year_model 
        self.__make = make
        self.__speed = speed

    # accelerate method add 5 each time it is called
    def accelerate(self):
        self.__speed += 5

    # brake method decrease 5 each time it is called 
    def brake(self):
        self.__speed -= 5

    # get current speed
    def current_speed(self):
        return self.__speed
    
    def display_speed(self):
        print("Speed: ", self.__speed, "kph")
