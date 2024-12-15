# POTD 9 test
import pytest
import subprocess

basename = "P09_dice"


def run_with_args(*args):
    try:
        command = ["python3", basename + ".py", *args]
        return subprocess.check_output(command, text=True).rstrip("\n")
    except:
        command = ["python", basename + ".py", *args]
        return subprocess.check_output(command, text=True).rstrip("\n")

def parse_output(output):
    """ Returns a 2-tuple with a list of ints and a float
    containing the reported individual rolls and the average."""
    values, avg = output.rstrip().split('\n')
    return [int(v) for v in values.split()], float(avg)

def test_basic_format():
    """ Make sure the output can be parsed and the right number
    of values are produced """
    values, avg = parse_output(run_with_args("6", "2"))
    assert len(values) == 2

def test_all_in_range():
    """ Test that all of the values are in the correct range """
    values, avg = parse_output(run_with_args("7", "2000"))
    for v in values:
        assert 1 <= v <= 7

def test_accurate_average():
    """ Test that the reported average is actually the average of the values"""
    values, avg = parse_output(run_with_args("10", "2000"))
    assert avg == pytest.approx(sum(values)/2000)

def test_distribution():
    """ Test that the distribution of values is approximately uniform."""
    values, avg = parse_output(run_with_args("8", "2000"))
    hist = dict(zip(range(1, 9), [0]*8)) # frequency histogram
    weight = 8 / 2000
    for v in values:
        hist[v] += weight
    assert hist == pytest.approx(dict(zip(range(1, 9), [1.0]*8)), rel=0.2)


pytest.main([basename + "_test.py", "-vv", "--showlocals", "-p", "no:faulthandler"])


