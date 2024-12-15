# POTD 6 test
import pytest
import subprocess

basename = "P06_time_convert"


def run_with_args(*args):
    try:
        command = ["python3", basename + ".py", *args]
        return subprocess.check_output(command, text=True).rstrip("\n")
    except:
        command = ["python", basename + ".py", *args]
        return subprocess.check_output(command, text=True).rstrip("\n")

def test_8am():
    assert run_with_args("8", "00", "AM") == "08:00"

def test_8pm():
    assert run_with_args("8", "00", "PM") == "20:00"
    
def test_1035pm():    
    assert run_with_args("10", "35", "PM") == "22:35"

def test_single_digit_minutes_am():
    assert run_with_args("11", "5", "AM") == "11:05"

def test_single_digit_minutes_pm():
    assert run_with_args("10", "8", "PM") == "22:08"
    
def test_noon():
    assert run_with_args("12", "00", "PM") == "12:00"

def test_midnight():    
    assert run_with_args("12", "00", "AM") == "00:00"
    
pytest.main([basename + "_test.py",  "-vv", "--showlocals", "-p", "no:faulthandler"])

