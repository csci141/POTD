# POTD 18 skel
import sys

def get_dictionary(code_file):
    """ Generate a morse code dictionary from code_file. Each line of the file
    contains a single character, a space, then a sequence of . and - characters
    comprising the code for that character. The returned dicationary maps each
    character to its code. As a special case, not included in the input file,
    the space character (" ") should map to the empty string ("").
    Parameters: code_file is the name of a file in the current directory with the morse code mappings for upper case letters
    Returns: a dictionary with characters (letters in upper case) as keys and the morse code string as values
    """

def reverse_dictionary(d):
    """ Build the reverse codebook for a given dictionary. Returns a new
    dictionary where each key is a value in d, and its value is the
    corresponding key in d. 
    Parameters: d is a dictionary
    Returns: a dictionary with keys and values reversed
    """

def translate_fwd(codebook, message):
    """ Translate from regular characters (A-Z, 0-9) to morse code using the
    given codebook, separating each code with a space. Unrecognized characters
    should be represented with a question mark (?). 
    Parameters: 
        codebook is a dictionary mapping characters (letters in upper case) to morse code
        message is a string of characters (letters in upper case)
    Returns: a string translated from characters to morse code
    """

def translate_rev(codebook, message):
    """ Translate from morse code characters back to regular characters using
    the given codebook whose keys are morse codes and values are characters.
    In the input message, the characters are separated by spaces, and words are
    separated by two spaces in a row. Unrecognized characters should be
    represented with a question mark (?).
    Parameters:
        codebook is a dictionary mapping morse code to characters (letters in upper case)
        message is a string of morse code
    Returns: a string translated from morse code to characters
    
    """


if __name__ == "__main__":
    pass

          
