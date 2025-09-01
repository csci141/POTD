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
        "args": ["900", "50"],
        "expected_output": "50.0 percent of 900.0 is 450.0"
    },
    {
        "args": ["900.0", "50.0"],
        "expected_output": "50.0 percent of 900.0 is 450.0"
    },
    {
        "args": ["120.0", "70"],
        "expected_output": "70.0 percent of 120.0 is 84.0"
    }
]

if __name__ == "__main__":
    run_assignment_tests("P03_percent.py", test_cases)