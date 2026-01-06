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
        "args": ["T", "T"],
        "expected_output": "False"
    },
    {
        "args": ["T", "F"],
        "expected_output": "True"
    },
    {
        "args": ["F", "T"],
        "expected_output": "True"
    },
    {
        "args": ["F", "F"],
        "expected_output": "False"
    }
]

if __name__ == "__main__":
    run_assignment_tests("P05_xor.py", test_cases)
