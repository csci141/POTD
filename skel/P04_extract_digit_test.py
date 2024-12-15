# POTD 4 
import pytest
import subprocess

basename = "P04_extract_digit"


def run_with_args(*args):
    try:
        command = ["python3", basename + ".py", *args]
        return subprocess.check_output(command, text=True).rstrip("\n")
    except:
        command = ["python", basename + ".py", *args]
        return subprocess.check_output(command, text=True).rstrip("\n")

def test_1():
    assert run_with_args("1531", "2") == "The 100s digit of 1531 is 5"
    
def test_2():    
    assert run_with_args("13", "0") == "The 1s digit of 13 is 3"
    
def test_3():    
    assert run_with_args("1300", "3") == "The 1000s digit of 1300 is 1"

pytest.main([basename + "_test.py",  "-vv", "--showlocals", "-p", "no:faulthandler"])
