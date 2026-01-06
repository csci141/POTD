try:
    from iotest import run_assignment_tests
    print("iotest found")
except ImportError:
    print("❌ Error: Could not find the 'iotest' module.")
    print("Please make sure 'iotest.py' is in the same directory as this test file and your solution program.")
    print("You can download 'iotest.py' from the github repository where POTD skeletons and test programs are found.")


try:
    import pytest
    print("pytest found")
except ImportError:
    print("❌ Error: Could not import the pytest module.")
    print("""Please make sure you have installed pytest. Please see the POTD Guide linked from Day 0 of the Schedule table for detailed instructions for one-time setup.""")

