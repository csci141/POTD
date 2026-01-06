# POTD 16 skel
# Author:
# Date:
# Description:

def encode_rle(input_file, rle_file):
    """ Read the given input file and write a run-length encoding of its
    contents to output_file. Each input line is run-length encoded
    independently and separated by newlines in the output.
    Returns the compression ratio - that is, the ratio of the output file's
    length to the input file's length. When counting file length, ignore
    newline characters.
    Precondition: input_file exists."""

    # implement this function

def decode_rle(rle_file, output_file):
    """ Decode the run-length encoded rle_file and write its decoded contents
    to output_file. Precondition: rle_file exists and is encoded according to
    the spec for encode_rle. """
    
    # implement this function


# Suggested helper functions 
# You may find it helpful to implement the functions below and use them in the
# above functions, but these are not directly tested by the test program.

def encode_line(line):
    """ Run-length encode a single line of text. """

def decode_line(line):
    """ Run-length decode a single line of text. """

