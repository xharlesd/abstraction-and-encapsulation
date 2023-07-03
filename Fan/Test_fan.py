from Fan_class import Fan

def fan_test():

    # create two fan objects
    fan1 = Fan()
    fan2 = Fan()

    fan1.set_speed(Fan.Fast_FS)
    fan1.set_radius(10)
    fan1.set_color('Yellow')
    fan1.set_status(True)