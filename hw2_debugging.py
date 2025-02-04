"""
This module provides functions to perform merge sort on an array and generate a random array.
"""

import secrets
import rand

def merge_sort_mrahma22(arr):
    """
    Sorts an array using the merge sort algorithm.

    Args:
        arr (list): A list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    if len(arr) <= 1:
        return arr

    half = len(arr)//2

    return recombine_mrahma22(merge_sort_mrahma22(arr[:half]), merge_sort_mrahma22(arr[half:]))

def recombine_mrahma22(left_arr, right_arr):
    """
    Recombines two sorted arrays into a single sorted array.

    Args:
        left_arr (list): The left sorted array.
        right_arr (list): The right sorted array.

    Returns:
        list: The recombined sorted array.
    """
    left_index = 0
    right_index = 0
    merge_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] <= right_arr[right_index]:
            merge_arr[merge_index] = left_arr[left_index]
            left_index += 1
            merge_index += 1
        else:
            merge_arr[merge_index] = right_arr[right_index]
            right_index += 1
            merge_index += 1

    for i in range(right_index, len(right_arr)):
        merge_arr[merge_index] = right_arr[i]
        merge_index += 1

    for i in range(left_index, len(left_arr)):
        merge_arr[merge_index] = left_arr[i]
        merge_index += 1


    return merge_arr

def custom_algo_mrahma22(n):
    """
    A custom algorithm that generates n fibonacci numbers.
    
    Args:
        n (int): The number of fibonacci numbers to generate.

    Returns:
        list: The list of n fibonacci numbers.
    """
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

arr_in = rand.random_array_mrahma22([None] * 20)
arr_out = merge_sort_mrahma22(arr_in)

print(arr_out)

print(custom_algo_mrahma22(secrets.randbelow(10)))
