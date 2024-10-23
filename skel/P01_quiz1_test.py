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
    stdout, stderr = process.communicate(input="\n")
    assert "What is" in stdout

pytest.main(["P01_quiz1_test.py", "-p", "no:faulthandler", "-v"])
