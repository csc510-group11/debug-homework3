"""
This module provides functionality to generate and print a random array.
"""
import secrets

def random_array_nafreen(arr):
    """
    Generates a random array from the given list of elements.

    Args:
        arr (list): The list of elements to be randomized.

    Returns:
        list: A new list containing the elements of arr in random order.
    """
    for i,_ in enumerate(arr):
        arr[i] = secrets.randbelow(20) + 1  # Generate a random number between 1 and 20
    return arr

def random_array_mrahma22(arr):
    """
    Replaces each element in the input array with a random integer between 1 and 20.

    Args:
        arr (list): A list of elements to be replaced with random integers.

    Returns:
        list: The modified list with random integers.
    """
    for i, _ in enumerate(arr):
        arr[i] = secrets.randbelow(20) + 1
    return arr
