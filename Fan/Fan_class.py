class Fan:
    # create constructor
    def __init__(self, speed = "Slow", radius = 5, color = "Blue", status = False):
        # instance variables
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__status = status
    
    # get fan speed
    def get_speed(self):
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
    def set_speed(self):
        if self.__speed == 1: 
            self.__speed == "Slow"
        elif self.__speed == 2: 
            self.__speed == "Medium"
        elif self.__speed == 3: 
            self.__speed == "Fast"

    # set fan status
    def set_status(self):
        self.__status == False

    # set fan radius
    def set_radius(self):
        return self.__radius

    # set fan color
    def set_color(self):
        return self.__color
    
        ""