#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    max_val = my_list[0]
    for element in my_list[1:]:
        if element > max_val:
            max_val = element
        return max_val