# POTD 8 test
import pytest
import subprocess

basename = "P08_calendar"

def run_with_args(*args):
    try:
        command = ["python3", basename + ".py", *args]
        return subprocess.check_output(command, text=True).rstrip("\n")
    except:
        command = ["python", basename + ".py", *args]
        return subprocess.check_output(command, text=True).rstrip("\n")
    
def remove_trailing_whitespace(output):
    """ Remove any trailing whitespace from the end of each line of output."""
    return '\n'.join([line.rstrip() for line in output.split('\n')])


def test_31_2():
    output = remove_trailing_whitespace(run_with_args("31", "2").rstrip())
    assert output == """su mo tu we th fr sa
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31"""

def test_28_6():
    output = remove_trailing_whitespace(run_with_args("28", "6").rstrip())
    assert output == """su mo tu we th fr sa
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28"""
    
def test_30_0():
    output = remove_trailing_whitespace(run_with_args("30", "0").rstrip())
    assert output == """su mo tu we th fr sa
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30"""
    
def test_31_4():
    output = remove_trailing_whitespace(run_with_args("31", "4").rstrip())
    assert output == """su mo tu we th fr sa
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31"""


pytest.main([basename + "_test.py",  "-vv", "--showlocals", "-p", "no:faulthandler"])

