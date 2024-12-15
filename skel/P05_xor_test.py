# POTD 5 test
import pytest
import subprocess

basename = "P05_xor"


def run_with_args(*args):
    try:
        command = ["python3", basename + ".py", *args]
        return subprocess.check_output(command, text=True).rstrip("\n")
    except:
        command = ["python", basename + ".py", *args]
        return subprocess.check_output(command, text=True).rstrip("\n")

def test_TT():
    assert run_with_args("T", "T") == "False"
    
def test_TF():    
    assert run_with_args("T", "F") == "True"
    
def test_FT():    
    assert run_with_args("F", "T") == "True"
    
def test_FF():    
    assert run_with_args("F", "F") == "False"


pytest.main([basename + "_test.py",  "-vv", "--showlocals", "-p", "no:faulthandler"])
