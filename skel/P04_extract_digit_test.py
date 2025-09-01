#!/usr/bin/env python3

try:
    from iotest import run_assignment_tests
except ImportError:
    print("❌ Error: Could not find the 'iotest' module.")
    print("Please make sure 'iotest.py' is in the same directory as this test file and your solution program.")
    print("You can download 'iotest.py' from the github repository where POTD skeletons and test programs are found.")
    exit(1)

test_cases = [
    {
        "args": ["1531", "2"],
        "expected_output": "The 100s digit of 1531 is 5"
    },
    {
        "args": ["13", "0"],
        "expected_output": "The 1s digit of 13 is 3"
    },
    {
        "args": ["1300", "3"],
        "expected_output": "The 1000s digit of 1300 is 1"
    }
]

if __name__ == "__main__":
    run_assignment_tests("P04_extract_digit.py", test_cases)
