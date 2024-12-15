#POTD 13 Test
import pytest
import subprocess

import P13_wrap

def test_fox_12():
    s = "The quick brown fox jumped over the lazy dog"
    assert P13_wrap.line_wrap(s, 12) == """\
The quick br
own fox jump
ed over the 
lazy dog"""
    
def test_fox_100():
    s = "The quick brown fox jumped over the lazy dog"
    assert P13_wrap.line_wrap(s, 100) == s
    
def test_fox_26():
    s = "The quick brown fox jumped over the lazy dog"
    assert P13_wrap.line_wrap(s, 26) == """\
The quick brown fox jumped
 over the lazy dog"""
    
def test_fox_4():
    s = "The quick brown fox jumped over the lazy dog"
    assert P13_wrap.line_wrap(s, 4) == """\
The 
quic
k br
own 
fox 
jump
ed o
ver 
the 
lazy
 dog"""

pytest.main(["P13_wrap_test.py", "-vv", "--showlocals", "-p", "no:faulthandler"])

