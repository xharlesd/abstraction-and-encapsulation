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
        if self.__speed == 1: 
            self.__speed == "Slow"
        elif self.__speed == 2: 
            self.__speed == "Medium"
        elif self.__speed == 3: 
            self.__speed == "Fast"

    # get fan status
    def get_status(self):
        return self.__status == False

    # get fan radius
    def get_radius(self):
        return self.__radius

    # get fan color
    def get_color(self):
        return self.__color
    

    # set fan speed

    # set fan status

    # set fan radius
    
    # set fan color
        ""