#!/usr/bin/python3
def safe_print_integer(value):
    pass
try:
    pass
except:
    pass
def safe_print_integer(value):
    try:
        pass
    except:
        pass
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except:
        return False
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except:
        return False