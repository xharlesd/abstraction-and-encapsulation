# Bernido, Charles David P. | BSCPE 1-5
# Object Oriented Programming | Assignment 9 - Problem 2

# import car class
from Car_class import Car
from colorama import Fore, Style

# create car object 
My_car = Car()

# call accelerate method five times and display current speed
print(Style.BRIGHT + Fore.YELLOW + "-"*16 + "\n   ACCELERATE\n" + "-"*16 + '\033[0m')
for i in range (5):
    My_car.accelerate()
    My_car.display_speed()

print(Style.BRIGHT + Fore.YELLOW + "\n" + "-"*16 + "\n     BRAKE\n" + "-"*16 + '\033[0m')
# call brake method five times and display current speed\
for i in range (5):
    My_car.brake()
    My_car.display_speed()