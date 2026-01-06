#!/usr/bin/env python3

import subprocess
import sys
import os
import shutil
import difflib


# Constants for formatting the output
class TColors:
    """Class to hold ANSI color codes for terminal output."""
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'


TIMEOUT_SECONDS = 2


def check_syntax(script_path):
    """
    Performs a pre-flight syntax check on the student's script.
    Returns True if syntax is valid, False if invalid.
    """
    if not os.path.exists(script_path):
        print(f"{TColors.RED}❌ Error: The script '{script_path}' was not found.{TColors.RESET}")
        print("Please make sure your script has the correct name and is in the same directory.")
        return False

    try:
        with open(script_path, 'r') as f:
            compile(f.read(), script_path, 'exec')
        return True
    except SyntaxError:
        print(f"{TColors.RED}Your program has a syntax error!{TColors.RESET}")
        print("Python could not understand your code. Please review your file for typos")
        print("or other syntax mistakes and run the test again. The tests were not run.")
        return False
    except Exception as e:
        print(f"{TColors.RED}An unexpected error occurred during syntax check: {e}{TColors.RESET}")
        return False


def print_test_result(passed, args_str):
    """
    Prints a formatted test result line with arguments.
    
    Args:
        passed (bool): Whether the test passed or failed
        args_str (str): String representation of the test arguments
    """
    if passed:
        print(f"{TColors.GREEN}[PASS] ✅ Arguments: {args_str}{TColors.RESET}")
    else:
        print(f"{TColors.RED}[FAIL] ❌ Arguments: {args_str}{TColors.RESET}")


def default_comparator(expected_output, actual_output):
    """
    Default comparator: compares expected and actual output line by line, stripping trailing whitespace.
    Returns (passed: bool, message: str). If not passed, message contains ndiff output.
    """
    expected_lines = [line.rstrip() for line in expected_output.split('\n')]
    actual_lines = [line.rstrip() for line in actual_output.split('\n')]
    passed = expected_lines == actual_lines
    if passed:
        return True, ""
    else:
        diff = difflib.ndiff(expected_lines, actual_lines)
        message_lines = []
        for line in diff:
            if line.startswith('- '):
                message_lines.append(f"{TColors.RED}{line}{TColors.RESET}")
            elif line.startswith('+ '):
                message_lines.append(f"{TColors.GREEN}{line}{TColors.RESET}")
            elif line.startswith('? '):
                message_lines.append(line)
        return False, "\n".join(f"    {l}" for l in message_lines)


def contains_comparator(expected_output, actual_output):
    """
    Comparator that checks if expected_output appears anywhere in actual_output.
    No whitespace stripping or line splitting.
    Returns (passed: bool, message: str).
    """
    if expected_output in actual_output:
        return True, ""
    else:
        msg = (
            f"    Expected output not found in observed output.\n"
            f"    --- Observed output ---\n"
            f"{actual_output}\n"
            f"    --- was expected to contain the following: ---\n"
            f"{expected_output}\n"
        )
        return False, msg


def run_tests(script_name, tests):
    """
    Runs the full suite of tests against the student's script.
    """
    passed_count = 0
    total_count = len(tests)

    for i, test in enumerate(tests):
        args = test["args"]
        expected_output = test["expected_output"].strip()
        stdin_input = test.get("stdin")  # Optional stdin input
        comparator = test.get("comparator", default_comparator)
        command = [sys.executable, script_name] + args
        args_str = " ".join(args)
        
        # Add stdin indicator to args string if present
        if stdin_input:
            args_str += f" (with stdin: {stdin_input})"

        try:
            # Prepare stdin data if provided
            stdin_data = None
            if stdin_input:
                stdin_data = "\n".join(stdin_input) + "\n"

            # Execute the student's script as a separate process
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                input=stdin_data,
                timeout=TIMEOUT_SECONDS,
                check=True  # This will raise CalledProcessError on non-zero exit codes
            )
            actual_output = result.stdout.strip()

            # Use the comparator function to check output
            passed, message = comparator(expected_output, actual_output)
            if passed:
                passed_count += 1
                print_test_result(True, args_str)
            else:
                print_test_result(False, args_str)
                print("  Differences:")
                print(message)

        except subprocess.TimeoutExpired:
            print_test_result(False, args_str)
            print(f"  Your program took longer than {TIMEOUT_SECONDS} seconds to run and was stopped.")
            print("  This might be caused by an infinite loop in your code.")

        except subprocess.CalledProcessError:
            print_test_result(False, args_str)
            print("  Your program crashed during this test (it returned a non-zero exit code).")
            print("  This is often caused by an unhandled error or exception.")

        except FileNotFoundError:
             # This should be caught by the pre-flight check, but is here as a failsafe
            print(f"{TColors.RED}Error: Could not find the script '{script_name}' to run.{TColors.RESET}")
            return # Stop testing if the script vanishes mid-run

    return passed_count, total_count


def run_assignment_tests(student_script_name, test_cases):
    """
    Main function to run tests for an assignment.
    
    Args:
        student_script_name (str): Name of the student's Python script
        test_cases (list): List of test case dictionaries with "args", "expected_output", and optionally "stdin"
    """
    print("--- Starting Test Runner ---")

    # Pre-flight syntax check
    if not check_syntax(student_script_name):
        passed, total = 0, len(test_cases) # no tests pass if syntax check fails
    else:  # passed the syntax check, run the tests
        passed, total = run_tests(student_script_name, test_cases)

    # Print final summary
    print("\n" + "-" * 28)
    print(f"Total: {passed} / {total} Tests Passed")
    print("-" * 28)

    if passed == total:
        print(f"{TColors.GREEN}All tests passed - nice work! 🎉{TColors.RESET}")

    return passed, total
