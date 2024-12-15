# POTD 20 test
import pytest
import copy
from P20_sort import swap, min_index, isort

@pytest.fixture
def test_lists():
    return [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [4],
        [3, 1],
        [4, 3, 6, -4, 10, -6],
        [-7, -7, -2, 7, 9, -9, -7, -1, 8, 8, -1, 4, -9, -5, -8, -4,
         10, -4, 5, -10, 5, 2, 4, 9, 3, -6, -6, 7, -6, 9, 4, 10, 5,
         -8, 1, 6, -1, 1, -3, 6, 3, -10, -1, 4, 2, -6, -5, -8, -3, 6]
    ]

def test_min_index(test_lists):
    test_lists = copy.deepcopy(test_lists)
    for lst in test_lists:
        fresh_lst = lst.copy()
        for start in range(0, len(lst)-1):
            for end in range(start+1, len(lst)):
                mi = min_index(lst, start, end)
                assert lst == fresh_lst, "min_index should not change its input list"
                assert lst[mi] == min(lst[start:end])
                
def test_swap(test_lists):
    swap_lists = copy.deepcopy(test_lists[:5])
    for lst in swap_lists:
        for i in range(0, len(lst)):
            for j in range(0, len(lst)):
                cpy = lst.copy()
                swap(cpy, i, j)
                assert cpy[j] == lst[i] and cpy[i] == lst[j], "elements not swapped properly"
                
                for k in range(len(cpy)):
                    if k != i and k != j:
                        assert cpy[k] == lst[k], "nonswapped elements should remain unchanged"

def test_sort(test_lists):
    sort_lists = copy.deepcopy(test_lists)
    for lst in sort_lists:
        for start in range(0, len(lst)-1):
            for end in range(start+1, len(lst)):
                fresh_lst = lst.copy()
                isort(fresh_lst, start, end)
                assert fresh_lst[start:end] == sorted(lst[start:end]), "not sorted correctly"
                assert lst[:start] == fresh_lst[:start], "list changed outside sort range"
                assert lst[end:] == fresh_lst[end:], "list changed outside sort range"

pytest.main(["P20_sort_test.py",   "-vv", "--showlocals", "-p", "no:faulthandler"])

