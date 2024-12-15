#POTD 2 test 
import pytest
import subprocess
import sys

def run_program(num1, num2):
    process = subprocess.Popen(
        [sys.executable, "P02_quiz2.py", str(num1), str(num2)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input="\n")
    return stdout.strip(), stderr, process.returncode

@pytest.mark.parametrize("num1,num2,expected", [
    (10, 4, "What is 10 * 4 ?\n10 * 4 is 40"),
    (5, 7, "What is 5 * 7 ?\n5 * 7 is 35"),
    (0, 8, "What is 0 * 8 ?\n0 * 8 is 0"),
    (3, -2, "What is 3 * -2 ?\n3 * -2 is -6"),
    (-4, -5, "What is -4 * -5 ?\n-4 * -5 is 20"),
])
def test_multiplication(num1, num2, expected):
    stdout, stderr, returncode = run_program(num1, num2)
    assert stdout == expected

pytest.main(["P02_quiz2_test.py", "-vv", "--showlocals", "-p", "no:faulthandler"])
