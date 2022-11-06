#!/usr/bin/python3

"""Function that adds 2 integers"""

def add_integer(a, b=98):
    """
    Adds 2 integers
    Args:
        a: first integer
        b: second integer
    Return: addition of the 2 integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
