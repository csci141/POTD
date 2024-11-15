# POTD 16 and 17 skel
import sys

def state_from_file(filename):
    """ Return the game state stored in the given file as a length-9 list.
    The file's first three rows contain a game state in the following format:
        x|x|x
        x|o|o
        o| |x
    Any additional lines of the file are ignored.
    The game state is returned as a length-9 list containing the three rows of
    the game, without the separator characters (|). The state list for the
    above game would be:
        ["x", "x", "x", "x", "o", "o", "o", " ", "x"]
    """

def get_row(state, i):
    """ Return a length-3 list containing the ith row of the game state.
    Rows are 0-indexed, so the rows are numbered 0, 1, and 2. """

def get_col(state, i):
    """ Return a length-3 list containing the ith column of the game state.
    Columns are 0-indexed, so the columns are numbered 0, 1, and 2. """

def get_diag(state, i):
    """ Return a length-3 list containing the ith diagonal of the game state.
    There are two diagonals:
      diagonal 0 is the one going from the top-left to the bottom-right
      diagonal 1 is the one going from the bottom-left to the top-right. """

   
def state_str(state):
    """ Return a string representation of the game state that matches the
    one read from the file, except with moves displayed as upper-case X and O
    """

def count_moves(state):
    """ Count the number of moves by either player that have been made so far
    in the game. For example, in the game state
        [' ', ' ', ' ', 'x', ' ', 'o', ' ', 'x', ' '],
    3 moves have been made. """

def analyze(state):
    """ Analyze the game state to determine which player (if any) has won, and
    where. Assume that the state represents a valid game state. This means at
    most one player has won. If no player has won, return None. If a player
    has won, return a length-3 tuple containing:
        - the winning player ("x" or "o", as a string)
        - the winning direction ("row", "column", or "diagonal")
        - the winning location (0, 1, or 2, defined as in the get_* functions.
    If a player has won in multiple places, any of the winning direction/locations
    can be returned."""

if __name__ == "__main__":
    pass
