from colorama import Fore, Style

# import pet class
from Pet_class import Pet

# asks the user to enter the name, type, and age of his or her pet
question = input(Fore.YELLOW + "\nHello! I'll just ask a few questions about your pet. Press enter to continue.")
pet_name = input(Fore.GREEN + "\nPlease enter your pet's name : " + Fore.YELLOW)
pet_type = input(Fore.GREEN + "Please input what type of animal is your pet : " + Fore.YELLOW) 
pet_age = input(Fore.GREEN + "Enter your pet's age : " + Fore.YELLOW)

# create Pet object
My_pet = Pet(pet_name, pet_type, pet_age)

# display the pet’s name, type, and age and display this data on the screen.
My_pet.display()