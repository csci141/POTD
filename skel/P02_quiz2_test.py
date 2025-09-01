# POTD 2 test using iotest
from iotest import run_assignment_tests

test_cases = [
    {
        "args": ["10", "4"],
        "expected_output": "What is 10 * 4 ?\n10 * 4 is 40\n",
        "stdin": [""],
    },
    {
        "args": ["5", "7"],
        "expected_output": "What is 5 * 7 ?\n5 * 7 is 35\n",
        "stdin": [""],
    },
    {
        "args": ["0", "8"],
        "expected_output": "What is 0 * 8 ?\n0 * 8 is 0\n",
        "stdin": [""],
    },
    {
        "args": ["3", "-2"],
        "expected_output": "What is 3 * -2 ?\n3 * -2 is -6\n",
        "stdin": [""],
    },
    {
        "args": ["-4", "-5"],
        "expected_output": "What is -4 * -5 ?\n-4 * -5 is 20\n",
        "stdin": [""],
    },
]

if __name__ == "__main__":
    run_assignment_tests("P02_quiz2.py", test_cases)

