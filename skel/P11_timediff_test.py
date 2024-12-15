# POTD 11 test
import pytest
import subprocess

from P11_timediff import (
    to_seconds,
    timediff
)

def test_to_seconds():
    assert to_seconds(0, 0, 0) == 0
    assert to_seconds(1, 0, 0) == 3600
    assert to_seconds(0, 1, 0) == 60
    assert to_seconds(0, 0, 1) == 1
    assert to_seconds(1, 1, 1) == 3661
    assert to_seconds(2, 3, 45) == 7425

def test_timediff():
    assert timediff(0, 0, 0, 1, 0, 0) == 3600
    assert timediff(1, 0, 0, 2, 0, 0) == 3600
    assert timediff(0, 0, 0, 0, 1, 0) == 60
    assert timediff(0, 0, 0, 0, 0, 1) == 1
    assert timediff(1, 30, 0, 2, 30, 0) == 3600
    assert timediff(10, 30, 0, 11, 45, 30) == 4530

pytest.main(["P11_timediff_test.py",  "-vv", "--showlocals", "-p", "no:faulthandler"])


