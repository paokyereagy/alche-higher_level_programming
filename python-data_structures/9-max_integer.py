#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    # Start with the first element as the current maximum
    max_val = my_list[0]

    # Compare each element to the current maximum
    for i in my_list[1:]:
        if i > max_val:
            max_val = i

    return max_val
