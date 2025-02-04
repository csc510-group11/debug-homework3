"""
This module provides functionality to generate and print a random array.
"""
import random

def random_array(arr):
    """
    Generates a random array from the given list of elements.

    Args:
        arr (list): The list of elements to be randomized.

    Returns:
        list: A new list containing the elements of arr in random order.
    """
    for i,_ in enumerate(arr):
        arr[i] = random.randint(1, 20)
    return arr
