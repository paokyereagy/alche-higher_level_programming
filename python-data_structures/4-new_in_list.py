#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Create a shallow copy of the list
    new_list = my_list[:]

    # Bounds checking
    if idx < 0:
        return new_list
    if idx >= len(new_list):
        return new_list

    # Replace element in the copy
    new_list[idx] = element
    return new_list
