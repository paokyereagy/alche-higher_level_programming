#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create a set of unique integers
    unique_integers = set(my_list)

    # Sum them manually without imports
    total = 0
    for val in unique_integers:
        total += val
    return total
