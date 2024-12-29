#POTD 1 test
import pytest
import subprocess
import sys

basename = "P01_quiz1"


def test_quiz1():
    process = subprocess.Popen(
        [sys.executable, "P01_quiz1.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    #When prompted for input, enter newline
    stdout, stderr = process.communicate(input="\n")

    #verify that the input prompt had 'What if' in the text string (capitalization and spacing matters!).
    assert "What is" in stdout

pytest.main(["P01_quiz1_test.py",  "-vv", "--showlocals", "-p", "no:faulthandler"])
