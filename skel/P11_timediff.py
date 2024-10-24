# POTD 11 skel
import sys

import P10_hms

def to_seconds(hours, minutes, seconds):
    """ Return the total number of seconds represented by a duration given as
    hours, minutes, and seconds."""

def timediff(h1, m1, s1, h2, m2, s2):
    """ Return the number of seconds between the two times
    h1:m1:s1 and h2:m2:s2, which are given as 3 integers representing a time
    in 24-hour format. Assume h2:m2:s2 is later than h1:m1:s1. """

if __name__ == "__main__":

    h1 = int(sys.argv[1])
    m1 = int(sys.argv[2])
    s1 = int(sys.argv[3])

    h2 = int(sys.argv[4])
    m2 = int(sys.argv[5])
    s2 = int(sys.argv[6])

    P10_hms.print_hms(timediff(h1, m1, s1, h2, m2, s2))
