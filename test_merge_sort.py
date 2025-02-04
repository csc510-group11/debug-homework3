from hw2_debugging import *

# Write 3 test cases for merge sort
def test_merge_sort():
    # Test case 1: Empty list
    assert merge_sort([]) == []
    # Test case 2: List with one element
    assert merge_sort([1]) == [1]
    # Test case 3: List with multiple elements
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
