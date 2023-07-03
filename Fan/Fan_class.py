class Fan:

    Slow_FS = 1
    Medium_FS = 2
    Fast_FS = 3

    # create constructor
    def __init__(self, speed = "Slow", radius = 5, color = "Blue", status = False):
        # instance variables
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__status = status
    
    # get fan speed
    def get_speed(self):
        self.__speed
        return self.__speed

    # get fan status
    def get_status(self):
        return self.__status
    
    # get fan radius
    def get_radius(self):
        return self.__radius
    
    # get fan color
    def get_color(self):
        return self.__color

    # set fan speed
    def set_speed(self, speed):
        self.__speed = speed

    # set fan status
    def set_status(self, status):
        self.__status = status

    # set fan radius
    def set_radius(self, radius):
        self.__radius = radius

    # set fan color
    def set_color(self, color):
        self.__color = color