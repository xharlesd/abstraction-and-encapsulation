# import car class
from Car_class import Car

# create car object 
My_car = Car()

# call accelerate method five times and display current speed
for i in range (5):
    My_car.accelerate()
    My_car.display_speed()

# call brake method five times and display current speed