# Bernido, Charles David P. | BSCPE 1-5
# Object Oriented Programming | Assignment 9 - Problem 1

from Fan_class import Fan
from colorama import Fore, Style

def fan_test():

    # create two fan objects
    fan1 = Fan()
    fan2 = Fan()

    # fan 1 properties
    fan1.set_speed(Fan.Fast_FS)
    fan1.set_radius(10)
    fan1.set_color('Yellow')
    fan1.set_status(True)
    
    print(Style.BRIGHT + Fore.GREEN + "-"*24 + "\n    FAN 1 PROPERTIES\n" + "-"*24 + '\033[0m')
    fan1.display_fan_properties()

    # fan 2 properties
    fan2.set_speed(Fan.Medium_FS)
    fan2.set_radius(5)
    fan2.set_color('Blue')
    fan2.set_status(False)

    print(Style.BRIGHT + Fore.GREEN + "-"*24 + "\n    FAN 2 PROPERTIES\n" + "-"*24 + '\033[0m')
    fan2.display_fan_properties()

fan_test()