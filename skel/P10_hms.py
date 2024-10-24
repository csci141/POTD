# POTD 10 skel
# Author:
# Date:
# Description:

import sys

def get_hours(seconds):
    """ Returns the integer number of hours contained in the given number of
    seconds. For example, 3662 represents 1 hour, 1 minute, and 2 seconds, so
    get_hours(3662) returns 1. Precondition: seconds >= 0. """


def get_minutes(seconds):
    """ Returns the integer number of minutes in the given number of seconds,
    not counting any minutes that contribute to a whole hour. For example,
    3662 represents 1 hour, 1 minute, and 2 seconds, so get_minutes(3662)
    returns 1. Precondition: seconds >= 0. """


def get_seconds(seconds):
    """ Returns the integer number of seconds in the given number of seconds,
    not counting any seconds that contribute to a minute or hour. For example,
    3662 represents 1 hour, 1 minute, and 2 seconds, so get_seconds(3662)
    returns 2. Precondition: seconds >= 0. """


def print_hms(seconds):
    """ Prints the given duration (provided in seconds) in hh:mm:ss format.
    Precondition: seconds >= 0 """

    
def padprint(number):
    """ Prints number zero-padded to 2 digits, by printing a zero before it if
    the number is only one digit. If the number is 2 or more digits, it's
    printed unmodified. No newline or space is
    printed after the number. Precondition: number >= 0. """
    

if __name__ == "__main__":
    pass # (this is a placeholder so the skeleton doesn't crash; delete it)
