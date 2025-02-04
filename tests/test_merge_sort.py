'''
This module provides functionality for merge sort.
'''
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from hw2_debugging import merge_sort # fixed: wildcard-import

# Write 3 test cases for merge sort
def test_merge_sort():
    '''
    Test cases for merge_sort function
    '''
    # Test case 1: Empty list
    if merge_sort([]) != []:
        raise AssertionError("The output array is not sorted correctly.") # fixed: CWE-703
    # Test case 2: List with one element
    if merge_sort([-9]) != [-9]:
        raise AssertionError("The output array is not sorted correctly.") # fixed: CWE-703
    # Test case 3: List with multiple elements
    if merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) != [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]:
        raise AssertionError("The output array is not sorted correctly.") # fixed: CWE-703
