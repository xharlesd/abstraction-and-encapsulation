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

    # getter methods
    # get name
    def set_name(self):
        return self.__name
    
    # get animal type
    def set_type(self):
       return self.__animal_type
    
    # get age
