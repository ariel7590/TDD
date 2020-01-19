
def valid_input(arg):
    if type(arg) == type(0.0) or type(arg) == type(0):
        if arg > 0:
            return True
    return False

