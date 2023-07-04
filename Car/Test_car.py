# import car class
from Car_class import Car

# create car object 
My_car = Car()

# call accelerate method five times and display current speed
print("---ACCELERATE---")
for i in range (5):
    My_car.accelerate()
    My_car.display_speed()

print("\n-----BRAKE-----")
# call brake method five times and display current speed\
for i in range (5):
    My_car.brake()
    My_car.display_speed()