# POTD 18 skel
import sys

def get_dictionary(code_file):
    """ Generate a morse code dictionary from code_file. Each line of the file
    contains a single character, a space, then a sequence of . and - characters
    comprising the code for that character. The returned dicationary maps each
    character to its code. As a special case, not included in the input file,
    the space character (" ") should map to the empty string (""). """

def reverse_dictionary(d):
    """ Build the reverse codebook for a given dictionary. Returns a new
    dictionary where each key is a value in d, and its value is the
    corresponding key in d. """

def translate_fwd(codebook, message):
    """ Translate from regular characters (a-z, 0-9) to morse code using the
    given codebook, separating each code with a space. Unrecognized characters
    should be represented with a question mark (?). """

def translate_rev(codebook, message):
    """ Translate from morse code characters back to regular characters using
    the given codebook whose keys are morse codes and values are characters.
    In the input message, the characters are separated by spaces, and words are
    separated by two spaces in a row. Unrecognized characters should be
    represented with a question mark (?)."""


if __name__ == "__main__":
    pass

          