#CSCI 141
#How to understand and use pytest programs

In this class, you will be assigned Program of the Days (POTD) that are used to help build your knowledge of 
coding. These programs are graded by pytest program that you should download to find out
if your POTD runs correctly. This will discuss how to use these and how troubleshoot with
them.

The first step is going to the class github. There you will find the folder "prompts' and 'skel'. 'prompts' folder has the instructions for each POTD,
and 'skel' has the starting skeleton file for the code and the test file. The skeleton file will be an outline you can use to
begin writing your code. The test file will check to see if it meets the assignment
requirements. The test file is used for grading, if you get 100% on the test file, you will get
100% on the assignment.

Download the files to your computer. It is highly advisable for this class that you set up a
folder on your computer to hold all of your code.

If you are unsure how to create a folder, there are many good tutorials online.

When you download the pytest program it may default to being saved in your downloads folder. Make sure to
move it to the folder that you save your POTD in to make sure it will run. If you do not have
the POTD in the same folder as the pytest program, your pytest will not run correctly. See more instructions in POTD1 for how to install and run pytest.

The next step of course is to write your program, but the pytest contains some very helpful
hints for your program.

Consider this pytest for POTD 1:

'''
#POTD 1 test
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
    #When prompted for input, enter newline
    stdout, stderr = process.communicate(input="\n")

    #verify that the input prompt had 'What if' in the text string (capitalization and spacing matters!).
    assert "What is" in stdout

pytest.main(["P01_quiz1_test.py",  "-vv", "--showlocals", "-p", "no:faulthandler"])

'''
The 'assert' statement indicates what it is looking for: in this case, it is looking for the string 'What is' to be printed to the screen as part of a user input request. 

When you design your program, the pytest shows you the
arguments your program should take as inputs, and the expected format of the output.
This can help you visualize what your code should look like once completed.

Make sure your code exactly matches the output. If it does not it will fail the pytest. This is
very important for tests in CSCI 141 and improving your coding skills. Your goal should be
to directly understand what the prompt is looking for and deliver a response that enables
you to fulfill that.

Once you’ve finished writing your POTD, open the pytest program and run it.

If it runs correctly, you should get a message that looks like this:

```
======================================= 3 passed in 0.35s =======================================
```

Congratulations, your code has finished the task. However often in this class you will find that
your code isn’t returning exactly what you’d like it to.

In this case you will receive an error message. Sometimes some of the test cases will pass,
and sometimes all of them will fail. Each failed test case will return an error message
describing why the test failed.

##Assert Error: Failed to meet the requirements of the test

This is the vaguest error. This will frequently happen when your code does not meet the
requirements. It could mean that your code is not returning or outputting the correct thing
at all. The pytest program is case sensitive and cares about all commas and periods. Make
sure that it has all of those. Review the exact output of the pytest program and check to see
if your program’s output matches the exact output the program is looking for. This error is
likely to occur because your code does not match the exact syntax of the output. Make
sure to go and review the exact syntax of the output in the pytest. There are POTD where
you will be expected to exactly match a program with newlines and placement of print
statements.

##Type Error: Code attempts to do an operation on a type that doesn't support that operation
(example, divide a string)

This error is very easy to fix. Find the portion of your code that is of the wrong type and use a
function, such as str(), int(), or float() to correct the error.

##Runtime Error: Code ran into a problem during its runtime (example, user inputs a string
when code expects an int)

This error is likely to occur because while using the sys.argv[] for your variable, the
arguments come in a string. This is easily corrected by applying the correct type function to
your variable to correct it.

##Indentation Error: The indentation of line(s) of code is incorrect (ex, 1 indent after starting
a for loop)

This error means that you forgot to properly indent your code. This is easily fixed. Just
check any loops or Boolean statements you are using to make sure that they all exactly
indent the way that you would like them to.
