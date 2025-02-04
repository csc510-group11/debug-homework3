"""
This module provides a function to replace elements in a list with random integers.

Functions:
    random_array(arr): Replaces each element in the input array with a random integer
    between 1 and 20.
"""
import secrets

def random_array(arr):
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
