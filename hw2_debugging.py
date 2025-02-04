"""
This module provides functionality to generate a random array.
"""
import rand # fixed: missing-module-docstring

def merge_sort_nafreen(arr): # fixed: Function name to snake_case naming style
    # fixed: missing-module-docstring
    # fixed: missing-function-docstring
    """
    Sorts an array in ascending order using the merge sort algorithm.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: A new list containing the sorted elements.
    """
    if len(arr) <= 1: # fixed: Unnecessary parens after 'if' keyword (superfluous-parens)
        return arr

    half = len(arr)//2

    return recombine_nafreen(merge_sort_nafreen(arr[:half]), merge_sort_nafreen(arr[half:]))

def recombine_nafreen(left_arr, right_arr): # fixed: Var name to snake_case style
    # fixed: missing-module-docstring
    # fixed: missing-function-docstring
    """
    Merges two sorted arrays into one sorted array.

    Args:
        left_arr (list): The first sorted array.
        right_arr (list): The second sorted array.

    Returns:
        list: A new list containing all elements from left_arr and right_arr, sorted.
    """
    left_index = 0 # fixed: Var name to snake_case style
    right_index = 0 # fixed: Var name to snake_case style
    merge_arr = [None] * (len(left_arr) + len(right_arr)) # fixed: Var name to snake_case style
    # print(f"left arr: {left_arr}, right arr: {right_arr}")
    arr_index = 0 # new variable index for merge_arr
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[arr_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[arr_index] = right_arr[right_index]
            right_index += 1
        arr_index += 1
        # print(f"left_index: {left_index}, right_index: {right_index}, merge_arr: {merge_arr}")
    for i in range(right_index, len(right_arr)): # fixed: Trailing whitespace (trailing-whitespace)
        merge_arr[arr_index] = right_arr[i]
        arr_index += 1
    for i in range(left_index, len(left_arr)): # fixed: Trailing whitespace (trailing-whitespace)
        merge_arr[arr_index] = left_arr[i]
        arr_index += 1
    # print("after merge_arr loop", merge_arr)
    # print('----------------------------------------------------------------')

    return merge_arr

# fixed: missing-function-docstring
def is_prime_function(n): # fixed: snake case naming convention
    """
    Checks if a number is prime.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if isinstance(n, float): # handled float values
        n = int(n)
    if isinstance(n, str): # handled string values
        print( "Input must be an integer.", end = " " )
        return False
    if n < 2: # handled values less than 2
        return False
    for i in range(2, int(n**0.5) + 1): # introduced optimization
        if n % i == 0:
            return False
    return True # fixed: trailing-whitespace

array = rand.random_array_nafreen([None] * 20) # fixed: Redefining name from outer scope
# print(array)
arr_out = merge_sort_nafreen(array)
print(arr_out) # fixed: Trailing whitespace (trailing-whitespace)
if arr_out != sorted(array):
    raise AssertionError("The output array is not sorted correctly.") # fixed: CWE-703
# fixed: Trailing newlines (trailing-newlines)

print(is_prime_function(17))  # Expected: True
print(is_prime_function(8))  # Expected: False
# fixed: If a float is passed, our function will break.
print(is_prime_function(17.89)) # Expected: True
# fixed: If a number less than 2 is passed, our function will return wrong output.
print(is_prime_function(-1)) # Expected: False
# fixed: If other datatype is passed, our function will break.
print(is_prime_function("ginger")) # Expected: False
