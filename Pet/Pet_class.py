from colorama import Fore, Style

# create pet class
class Pet:
    # constructor
    def __init__(self, name, animal_type, age):
        # instance variables
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # setter methods
    # set name
    def set_name(self, name):
        self.__name = name

    # set animal type
    def set_type(self, animal_type):
        self.__animal_type = animal_type

    # set age
    def set_age(self, age):
        self.__age = age


    # getter methods
    # get name
    def set_name(self):
        return self.__name
    
    # get animal type
    def set_type(self):
        return self.__animal_type
    
    # get age
    def set_age(self):
        return self.__age
    
    def display(self):
        print(Style.BRIGHT + Fore.MAGENTA + "\n" + "-"*24 + "\n        PET INFO\n" + "-"*24 + '\033[0m')
        print(Style.BRIGHT + Fore.YELLOW + "  Pet's Name  :" + '\033[0m', Style.BRIGHT + Fore.CYAN, self.__name)
        print(Fore.YELLOW + "  Animal Type :" + '\033[0m', Style.BRIGHT + Fore.CYAN, self.__animal_type)
        print(Fore.YELLOW + "  Pet's Age   :" + '\033[0m', Style.BRIGHT + Fore.CYAN, self.__age)
        print(Style.BRIGHT + Fore.MAGENTA +"-"*24 + '\033[0m' + "\n")