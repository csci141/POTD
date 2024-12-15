# POTD 12 skel
import pytest
import subprocess
from P12_timeconflict import to_seconds, to_hms, conflicts

basename = "P12_timeconflict"

def test_to_seconds():
    assert to_seconds((0, 0, 0)) == 0
    assert to_seconds((1, 0, 0)) == 3600
    assert to_seconds((0, 1, 0)) == 60
    assert to_seconds((0, 0, 1)) == 1
    assert to_seconds((2, 30, 45)) == 9045

def test_to_hms():
    assert to_hms(0) == (0, 0, 0)
    assert to_hms(3600) == (1, 0, 0)
    assert to_hms(60) == (0, 1, 0)
    assert to_hms(1) == (0, 0, 1)
    assert to_hms(9045) == (2, 30, 45)

def test_conflicts():
    assert conflicts((10, 0, 0), (11, 0, 0), (10, 30, 0)) == True
    assert conflicts((10, 0, 0), (11, 0, 0), (9, 59, 59)) == False
    assert conflicts((10, 0, 0), (11, 0, 0), (11, 0, 0)) == True
    assert conflicts((10, 0, 0), (11, 0, 0), (11, 0, 1)) == False
    assert conflicts((8, 0, 0), (17, 0, 0), (12, 0, 0)) == True
    assert conflicts((8, 0, 0), (17, 0, 0), (7, 59, 59)) == False
    assert conflicts((8, 0, 0), (17, 0, 0), (17, 0, 1)) == False


def run_with_args(*args):
    try:
        command = ["python3", basename + ".py", *args]
        return subprocess.check_output(command, text=True).rstrip("\n")
    except:
        command = ["python", basename + ".py", *args]
        return subprocess.check_output(command, text=True).rstrip("\n")

def test_main_program():
    assert run_with_args("10", "0", "0", "11", "0", "0", "10", "30", "0") == \
        "(10, 30, 0) conflicts with the interval from (10, 0, 0) to (11, 0, 0)"

    assert run_with_args("10", "0", "0", "11", "0", "0", "12", "0", "0") == \
        "(12, 0, 0) does not conflict with the interval from (10, 0, 0) to (11, 0, 0)"
    
pytest.main([basename + "_test.py",  "-vv", "--showlocals", "-p", "no:faulthandler"])
