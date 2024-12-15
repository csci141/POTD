# POTD 3 test
import pytest
import subprocess

basename = "P03_percent"


def run_with_args(*args):
    try:
        command = ["python3", basename + ".py", *args]
        return subprocess.check_output(command, text=True).rstrip("\n")
    except:
        command = ["python", basename + ".py", *args]
        return subprocess.check_output(command, text=True).rstrip("\n")

def test_1():
    assert run_with_args("900", "50") == "50.0 percent of 900.0 is 450.0"
    
def test_2():    
    assert run_with_args("900.0", "50.0") == "50.0 percent of 900.0 is 450.0"
    
def test_3():    
    assert run_with_args("120.0", "70") == "70.0 percent of 120.0 is 84.0"


pytest.main([basename + "_test.py", "-vv", "--showlocals", "-p", "no:faulthandler"])