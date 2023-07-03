from Fan_class import Fan

def fan_test():

    # create two fan objects
    fan1 = Fan()
    fan2 = Fan()

    # fan 1 properties
    fan1.set_speed(Fan.Fast_FS)
    fan1.set_radius(10)
    fan1.set_color('Yellow')
    fan1.set_status(True)
    print("FAN 1 PROPERTIES")
    fan1.display_fan_properties()

    # fan 2 properties
    fan2.set_speed(Fan.Medium_FS)
    fan2.set_radius(5)
    fan2.set_color('Blue')
    fan2.set_status(False)
    print("\nFAN 2 PROPERTIES")
    fan2.display_fan_properties()

fan_test()