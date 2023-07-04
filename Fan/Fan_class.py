from colorama import Fore, Style

class Fan:

    # Three constants to denote fan speed
    Slow_FS = 1
    Medium_FS = 2
    Fast_FS = 3

    # create constructor
    def __init__(self, speed = Slow_FS, radius = 5, color = "Blue", status = False):
        # instance variables
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__status = status
    
    # accessor(getters)
    # get fan speed
    def get_speed(self):
        return self.__speed

    # get fan status
    def get_status(self):
        return self.__status
    
    # get fan radiusS
    def get_radius(self):
        return self.__radius
    
    # get fan color
    def get_color(self):
        return self.__color

    # mutator(setters)
    # set fan speed
    def set_speed(self, speed):
        self.__speed = speed

    # set fan status
    def set_status(self, status):
        self.__status = bool(status)

    # set fan radius
    def set_radius(self, radius):
        self.__radius = float(radius)

    # set fan color
    def set_color(self, color):
        self.__color = str(color)

    def display_fan_properties(self):
        print(Style.BRIGHT + Fore.CYAN + "Speed      :  " + '\033[0m', Fore.YELLOW, self.__speed)
        print(Style.BRIGHT + Fore.CYAN + "Radius     :  " + '\033[0m', Fore.YELLOW, self.__radius)
        print(Style.BRIGHT + Fore.CYAN + "Color      :  " + '\033[0m', Fore.YELLOW, self.__color)
        print(Style.BRIGHT + Fore.CYAN + "Status(ON) :  " + '\033[0m', Fore.YELLOW, self.__status, '\033[0m')