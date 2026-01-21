#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_elements = []
    for element in my_list:
        if element not in unique_elements:
            unique_elements.append(element)
            total = 0
    for element in unique_elements:
        total += element
    return total