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
        "args": ["4"],
        "expected_output": "3"
    },
    {
        "args": ["14"],
        "expected_output": "4"
    },
    {
        "args": ["1"],
        "expected_output": "1"
    },
    {
        "args": ["16383"],
        "expected_output": "14"
    },
    {
        "args": ["16384"],
        "expected_output": "15"
    },
    {
        "args": ["0"],
        "expected_output": "1"
    }
]

if __name__ == "__main__":
    run_assignment_tests("P07_binarydigits.py", test_cases)

