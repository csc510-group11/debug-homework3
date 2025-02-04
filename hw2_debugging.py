"""
This module provides functionality to generate a random array.
"""
import rand # Fixed: missing-module-docstring

def merge_sort(arr): # fixed: Function name to snake_case naming style
    # Fixed: missing-module-docstring
    # Fixed: missing-function-docstring
    """
    Sorts an array in ascending order using the merge sort algorithm.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: A new list containing the sorted elements.
    """
    if len(arr) == 1: # fixed: Unnecessary parens after 'if' keyword (superfluous-parens)
        return arr

    half = len(arr)//2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))

def recombine(left_arr, right_arr): # fixed: Var name to snake_case style
    # Fixed: missing-module-docstring
    # Fixed: missing-function-docstring
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

array = rand.random_array([None] * 20) # fixed: Redefining name from outer scope
# print(array)
arr_out = merge_sort(array)
print(arr_out) # fixed: Trailing whitespace (trailing-whitespace)
assert arr_out == sorted(array)
# fixed: Trailing newlines (trailing-newlines)
