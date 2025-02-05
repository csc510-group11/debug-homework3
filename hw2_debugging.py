"""
This module provides functionality to generate a random array.
"""
import secrets
import rand  # fixed: missing-module-docstring


def merge_sort_nafreen(arr):  # fixed: Function name to snake_case naming style
    # fixed: missing-module-docstring
    # fixed: missing-function-docstring
    """
    Sorts an array in ascending order using the merge sort algorithm.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: A new list containing the sorted elements.
    """
    if len(arr) <= 1:  # fixed: Unnecessary parens after 'if' keyword (superfluous-parens)
        return arr

    half = len(arr) // 2

    return recombine_nafreen(merge_sort_nafreen(
        arr[:half]), merge_sort_nafreen(arr[half:]))


def recombine_nafreen(left_arr, right_arr):  # fixed: Var name to snake_case style
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
    left_index = 0  # fixed: Var name to snake_case style
    right_index = 0  # fixed: Var name to snake_case style
    # fixed: Var name to snake_case style
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    # print(f"left arr: {left_arr}, right arr: {right_arr}")
    arr_index = 0  # new variable index for merge_arr
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[arr_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[arr_index] = right_arr[right_index]
            right_index += 1
        arr_index += 1
        # print(f"left_index: {left_index}, right_index: {right_index}, merge_arr: {merge_arr}")
    for i in range(right_index, len(right_arr)
                   ):  # fixed: Trailing whitespace (trailing-whitespace)
        merge_arr[arr_index] = right_arr[i]
        arr_index += 1
    for i in range(left_index, len(left_arr)
                   ):  # fixed: Trailing whitespace (trailing-whitespace)
        merge_arr[arr_index] = left_arr[i]
        arr_index += 1
    # print("after merge_arr loop", merge_arr)
    # print('----------------------------------------------------------------')

    return merge_arr

# fixed: missing-function-docstring


def is_prime_function(n):  # fixed: snake case naming convention
    """
    Checks if a number is prime.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if isinstance(n, float):  # handled float values
        n = int(n)
    if isinstance(n, str):  # handled string values
        print("Input must be an integer.", end=" ")
        return False
    if n < 2:  # handled values less than 2
        return False
    for i in range(2, int(n**0.5) + 1):  # introduced optimization
        if n % i == 0:
            return False
    return True  # fixed: trailing-whitespace


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

    half = len(arr) // 2

    return recombine_mrahma22(merge_sort_mrahma22(
        arr[:half]), merge_sort_mrahma22(arr[half:]))


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
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


def merge_sort_sdatta4(arr):
    """
    Sort a array using the merge sort algorithm 
    """
    if len(arr) == 1:
        return arr

    half = len(arr) // 2

    return recombine_sdatta4(merge_sort_sdatta4(
        arr[:half]), merge_sort_sdatta4(arr[half:]))


def recombine_sdatta4(left_arr, right_arr):
    """
    Recombines array for merge sorting
    """
    left_index = 0
    right_index = 0
    merge_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[merge_index] = left_arr[left_index]
            left_index += 1
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

def bubble_sort_sdatta4(arr):
    """
    Performs bubble sort on a array
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# fixed: Redefining name from outer scope
array = rand.random_array_nafreen([None] * 20)
# print(array)
arr_out = merge_sort_nafreen(array)
print(arr_out)  # fixed: Trailing whitespace (trailing-whitespace)
if arr_out != sorted(array):
    raise AssertionError(
        "The output array is not sorted correctly.")  # fixed: CWE-703
# fixed: Trailing newlines (trailing-newlines)

print(is_prime_function(17))  # Expected: True
print(is_prime_function(8))  # Expected: False
# fixed: If a float is passed, our function will break.
print(is_prime_function(17.89))  # Expected: True
# fixed: If a number less than 2 is passed, our function will return wrong
# output.
print(is_prime_function(-1))  # Expected: False
# fixed: If other datatype is passed, our function will break.
print(is_prime_function("ginger"))  # Expected: False

arr_in = rand.random_array_mrahma22([None] * 20)
arr_out = merge_sort_mrahma22(arr_in)

print(arr_out)

print(custom_algo_mrahma22(secrets.randbelow(10)))

data = rand.random_array_sdatta4([None] * 20)
print(data)
arr_out = merge_sort_sdatta4(data)
print(arr_out)

arr_out = bubble_sort_sdatta4(data)
print(arr_out)
