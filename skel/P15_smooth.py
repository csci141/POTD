# POTD 15 skel
import sys

def mean(nums):
    """ Return the arithmetic mean (i.e., average) of the list of numbers
    nums. Precondition: nums is not empty and contains only numbers.
    Does not modify its input (nums). """

def smooth(nums):
    """ Return a smoothed copy of nums, where each element in the resulting
    list is the average of its old value and its two neighbors. The neighbor
    relation "wraps": that is, the first element's left neighbor should be the
    last element, and similarly the last element's right neighbor is the first
    element. For example, if we call smooth([a, b, c, d]), it should return a
    list [a', b', c', d'], where:
        a' is the average of d, a, and b
        b' is the average of a, b, and c
        c' is the average of b, c, and d
        d' is the average of c, d, and a
    Preconditions: nums contains only numbers and has length at least 3.
    This function does *not* modify the input list (nums)."""


def print_rounded(nums, end="\n"):
    """ Prints a list of numbers, rounded to the given number of decimal
    places. Does not modify nums. This function is provided for you
    and is only needed for use in the main program. You are not required
    to understand the details of how it works. """ 
    print("[", end="")
    for i in range(len(nums)-1):
        print(f"{nums[i]:3.2f}", end=", ")
    print(f"{nums[-1]:3.2f}]", end=end)

if __name__ == "__main__":
    pass # (this is a placeholder so the skeleton doesn't crash; delete it)
