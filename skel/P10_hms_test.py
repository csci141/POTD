# POTD 10 test
import pytest
import subprocess

from P10_hms import (
    get_hours,
    get_minutes,
    get_seconds,
    print_hms,
    padprint
)

def test_get_hours():
    assert get_hours(0) == 0
    assert get_hours(3599) == 0
    assert get_hours(3600) == 1
    assert get_hours(3662) == 1
    assert get_hours(7200) == 2

def test_get_minutes():
    assert get_minutes(0) == 0
    assert get_minutes(59) == 0
    assert get_minutes(60) == 1
    assert get_minutes(3662) == 1
    assert get_minutes(7320) == 2

def test_get_seconds():
    assert get_seconds(0) == 0
    assert get_seconds(59) == 59
    assert get_seconds(60) == 0
    assert get_seconds(3662) == 2
    assert get_seconds(7322) == 2

def test_print_hms(capsys):
    print_hms(3662)
    captured = capsys.readouterr()
    assert captured.out.strip() == "01:01:02"

    print_hms(7322)
    captured = capsys.readouterr()
    assert captured.out.strip() == "02:02:02"

def test_padprint(capsys):
    padprint(5)
    captured = capsys.readouterr()
    assert captured.out == "05"

    padprint(10)
    captured = capsys.readouterr()
    assert captured.out == "10"
    
    padprint(124)
    captured = capsys.readouterr()
    assert captured.out == "124"

def test_mainguard(capsys):
    
    command = ["python", "-c", "import P10_hms"]
    message = "importing P10_hms should not print any output or cause an error; check your main guard"
    try:
        assert subprocess.check_output(command, text=True) == "", message
    except subprocess.CalledProcessError:
        assert False, message
    except FileNotFoundError:
        command = ["python3", "-c", "import P10_hms"]
        try:
            assert subprocess.check_output(command, text=True) == "", message
        except subprocess.CalledProcessError:
            assert False, message

def test_mainprogram():
    try:
      command = ["python3", "P10_hms.py", "7333"]
      output = subprocess.check_output(command, text=True).rstrip("\n")
    except Exception:
      command = ["python", "P10_hms.py", "7333"]
      output = subprocess.check_output(command, text=True).rstrip("\n")
    
    assert output == "02:02:13"

pytest.main(["P10_hms_test.py", "-vv", "--showlocals", "-p", "no:faulthandler"])


