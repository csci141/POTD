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
        "args": ["8", "00", "AM"],
        "expected_output": "08:00"
    },
    {
        "args": ["8", "00", "PM"],
        "expected_output": "20:00"
    },
    {
        "args": ["10", "35", "PM"],
        "expected_output": "22:35"
    },
    {
        "args": ["11", "5", "AM"],
        "expected_output": "11:05"
    },
    {
        "args": ["10", "8", "PM"],
        "expected_output": "22:08"
    },
    {
        "args": ["12", "00", "PM"],
        "expected_output": "12:00"
    },
    {
        "args": ["12", "00", "AM"],
        "expected_output": "00:00"
    }
]

if __name__ == "__main__":
    run_assignment_tests("P06_time_convert.py", test_cases)

