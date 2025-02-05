import sys
import os
import random

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))


from hw2_debugging import merge_sort_sdatta4 as merge_sort

def test_merge_sort_empty():
    assert merge_sort([]) == []

def test_merge_sort_single_element():
    assert merge_sort([1,1,1,1,1,1,1]) == [1,1,1,1,1,1,1]

def test_merge_sort_multiple_elements():
    assert merge_sort(None) == []

def test_merge_sort_single_element():
    arr = random.sample(range(3000),2000)
    sorted_arr = arr.copy() 
    sorted_arr.sort()
    assert merge_sort(arr) == sorted_arr