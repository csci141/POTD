# POTD 14 test
import pytest
import subprocess

from P14_rotcipher import rotate

upper_alphabet = ''.join([chr(x) for x in range(ord('A'), ord('Z')+1)])
lower_alphabet = ''.join([chr(x) for x in range(ord('a'), ord('z')+1)])

def test_ABC1():
    assert rotate(1, "ABC") == "BCD"
    
def test_XYZ1():
    assert rotate(1, "XYZ") == "YZA"

def test_xyz2():
    assert rotate(2, "xyz") == "ZAB"

def test_upper13():
    assert rotate(13, upper_alphabet) == upper_alphabet[13:] + upper_alphabet[:13]

def test_lower13():
    assert rotate(13, lower_alphabet) == upper_alphabet[13:] + upper_alphabet[:13]

def test_nonalpha():
    assert rotate(10, "A Hard Rain's A-Gonna Fall") == "K RKBN BKSX'C K-QYXXK PKVV"
    
def test_circular():
    assert rotate(6, rotate(20, "SECRET PASSWORD")) == "SECRET PASSWORD"

pytest.main(["P14_rotcipher_test.py", "-vv", "--showlocals", "-p", "no:faulthandler"])