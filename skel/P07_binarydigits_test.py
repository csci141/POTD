# POTD 7 test
import pytest
import subprocess

basename = "P07_binarydigits"


def run_with_args(*args):
    try:
        command = ["python3", basename + ".py", *args]
        return subprocess.check_output(command, text=True).rstrip("\n")
    except:
        command = ["python", basename + ".py", *args]
        return subprocess.check_output(command, text=True).rstrip("\n")

def test_4():
    # 4 in binary is 100
    assert run_with_args("4") == "3"
    
def test_14():
    # 14 in binary is 1101
    assert run_with_args("14") == "4"
    
def test_1():
    # 1 in binary is 1
    assert run_with_args("1") == "1"

def test_16383():
    # 16,383 in binary is 11111111111111
    assert run_with_args("16383") == "14"
    
def test_16384():
    # 16,384 in binary is 100000000000000
    assert run_with_args("16384") == "15"

def test_0():
    #0 in binary is 0
    assert run_with_args("0") == "1"

pytest.main([basename + "_test.py",  "-vv", "--showlocals", "-p", "no:faulthandler"])

