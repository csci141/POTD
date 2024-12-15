# POTD 15 test
import pytest

from P15_smooth import mean, smooth

test_cases = [ # list of tuples, containing (input, true mean, true smoothed)
    ([1.0, 1.0, 1.0], 1.0, [1.0, 1.0, 1.0]),
    ([1.0, 2.0, 3.0], 2.0, [2.0, 2.0, 2.0]),
    ([1.0, 2.0, 3.0, 4.0, 5.0], 3.0, [2.6666666666666665, 2.0, 3.0, 4.0, 3.3333333333333335]),
    ([8.0, 6.0, 2.5, 1.0, -1.0, -0.9], 2.6, [4.366666666666666, 5.5, 3.1666666666666665, 0.8333333333333334, -0.3, 2.033333333333333])
]

# Helpers
def smooth_correct(nums_in, true_out):
    smoothed = smooth(nums_in)
    assert smoothed == pytest.approx(true_out)

def mean_correct(nums_in, true_mean):
    assert mean(nums_in) == pytest.approx(true_mean)
    
def test_111mean():
    nums_in, true_mean, _ = test_cases[0]
    mean_correct(nums_in, true_mean)
    
def test_111smooth():
    nums_in, _, true_smoothed = test_cases[0]
    smooth_correct(nums_in, true_smoothed)
    
def test_123mean():
    nums_in, true_mean, _ = test_cases[1]
    mean_correct(nums_in, true_mean)
    
def test_123smooth():
    nums_in, _, true_smoothed = test_cases[1]
    smooth_correct(nums_in, true_smoothed)
    
def test_12345mean():
    nums_in, true_mean, _ = test_cases[2]
    mean_correct(nums_in, true_mean)
    
def test_12345smooth():
    nums_in, _, true_smoothed = test_cases[2]
    smooth_correct(nums_in, true_smoothed)
    
def test_86etc_mean():
    nums_in, true_mean, _ = test_cases[3]
    mean_correct(nums_in, true_mean)
    
def test_86etc_smooth():
    nums_in, _, true_smoothed = test_cases[3]
    smooth_correct(nums_in, true_smoothed)

def test_nomodify(): # make sure neither function modifies its input list
    for case in test_cases:
        nums_in = case[0]
        orig = nums_in[:]
        
        avg = mean(nums_in)
        assert nums_in == orig, "mean should not modify its input"
        
        smoothed = smooth(nums_in)
        assert nums_in == orig, "smooth and should not modify its input"

pytest.main(["P15_smooth_test.py", "-vv", "--showlocals", "-p", "no:faulthandler"])