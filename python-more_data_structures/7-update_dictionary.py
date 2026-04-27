#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    # Assign the value to the key directly
    # If the key exists, it will be replaced
    # If the key does not exist, it will be created
    a_dictionary[key] = value
    return a_dictionary
