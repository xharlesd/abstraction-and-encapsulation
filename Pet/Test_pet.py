# import pet class
from Pet_class import Pet

# asks the user to enter the name, type, and age of his or her pet
pet_name = input("Please enter your pet's name: ")
pet_type = input("Please input animal type of your pet: ") 
pet_age = input("Enter your pet's age: ")

# create Pet object
My_pet = Pet(pet_name, pet_type, pet_age)

# display the pet’s name, type, and age and display this data on the screen.