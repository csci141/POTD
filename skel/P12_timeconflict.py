# POTD 12 skel
import sys

def to_seconds(hms_tuple):
    """ Returns the total number of seconds represented by a duration given as
    a 3-tuple containing (hours, minutes, and seconds). """

def to_hms(seconds):
    """ Returns a tuple of (hours, minutes, seconds) for the given
    raw number of seconds. Precondition: seconds >= 0. """
    
def conflicts(start_time, end_time, query_time):
    """ Returns whether query_time is inside the interval from start_time to
    end_time, including the endpoints. Preconditions: Input times are given
    as 3-tuples of (hour, minute, second) in 24h format, and start_time is
    before end_time (on the same day). """


if __name__ == "__main__":
    start_t = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    end_t   = int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
    query_t = int(sys.argv[7]), int(sys.argv[8]), int(sys.argv[9])
    
    # complete the main program here