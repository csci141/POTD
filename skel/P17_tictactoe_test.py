# POTD 17 test
import pytest
import pathlib
# import pickle

from P17_tictactoe import *

N_TEST_GAMES = 7

@pytest.fixture(scope="module")
def test_games():
    return [
###### test game 0
{"input": """\
x| |o
x|o|o
o| |x""",
"state": 
['x',' ','o',
 'x','o','o',
 'o',' ','x'],
"state_str":"""\
X| |O
X|O|O
O| |X""",
"moves": 7,
"win": ['o', 'diagonal', 1],
"rows": [
['x', ' ', 'o'],
['x', 'o', 'o'],
['o', ' ', 'x']],
"cols": [
['x', 'x', 'o'],
[' ', 'o', ' '],
['o', 'o', 'x']],
"diags": [
['x', 'o', 'x'],
['o', 'o', 'o']],
},
###### test game 1
{"input": """\
o| |o
x|o|o
x|x|x""",
"state": 
['o',' ','o',
 'x','o','o',
 'x','x','x'],
"state_str":"""\
O| |O
X|O|O
X|X|X""",
"moves": 8,
"win": ['x', 'row', 2],
},
###### test game 2
{"input": """\
o|o|x
o|x|o
x|x|o""",
"state": 
['o','o','x',
 'o','x','o',
 'x','x','o'],
"state_str":"""\
O|O|X
O|X|O
X|X|O""",
"moves": 9,
"win": ['x', 'diagonal', 1],
},
###### test game 3
{"input": """\
o| |x
x|o| 
x|o|o""",
"state": 
['o',' ','x',
 'x','o',' ',
 'x','o','o'],
"state_str":"""\
O| |X
X|O| 
X|O|O""",
"moves": 7,
"win": ['o', 'diagonal', 0],
},
###### test game 4
{"input": """\
x|x|o
o|x|x
o|x|o""",
"state": 
['x','x','o',
 'o','x','x',
 'o','x','o'],
"state_str":"""\
X|X|O
O|X|X
O|X|O""",
"moves": 9,
"win": ['x', 'column', 1],
},
###### test game 5
{"input": """\
 | | 
 | | 
 | | """,
"state": 
[' ',' ',' ',
 ' ',' ',' ',
 ' ',' ',' '],
"state_str":"""\
 | | 
 | | 
 | | """,
"moves": 0,
"win": None,
},
###### test game 6
{"input": """\
 | | 
 |x| 
 | | """,
"state": 
[' ',' ',' ',
 ' ','x',' ',
 ' ',' ',' '],
"state_str":"""\
 | | 
 |X| 
 | | """,
"moves": 1,
"win": None,
},
]

# @pytest.fixture(scope="module")
# def test_games():
#     with open("P16_17_test_data.pkl", "rb") as f:
#         return pickle.loads(f.read())

game_dir = pathlib.Path("./P17_games")

@pytest.fixture(scope="module")
def input_files(test_games):
    game_dir.mkdir(exist_ok=True)
    
    # Create a file for each test case
    file_mapping = {}
    for i, game in enumerate(test_games):
        test_file = game_dir / f"P17_game{i}.txt"
        test_file.write_text(game["input"])
        file_mapping[i] = test_file
    
    return file_mapping

@pytest.mark.parametrize("test_game_index", range(N_TEST_GAMES))
def test_state_from_file(input_files, test_games, test_game_index):
    test_file = input_files[test_game_index]
    result_state = state_from_file(str(test_file))
    assert result_state == test_games[test_game_index]["state"]

    
def test_get_row(test_games):
    tz = test_games[0]
    for r in range(3):
        assert get_row(tz["state"], r) == tz["rows"][r]


def test_get_col(test_games):
    tz = test_games[0]
    for c in range(3):
        assert get_col(tz["state"], c) == tz["cols"][c]
        
def test_get_diag(test_games):
    tz = test_games[0]
    for d in range(2):
        assert get_diag(tz["state"], d) == tz["diags"][d]     

@pytest.mark.parametrize("test_game_index", range(N_TEST_GAMES))
def test_state_str(test_games, test_game_index):
    test_game = test_games[test_game_index]
    assert state_str(test_game["state"]) == test_game["state_str"]

@pytest.mark.parametrize("test_game_index", range(N_TEST_GAMES))
def test_count_moves(test_games, test_game_index):
    test_game = test_games[test_game_index]
    assert count_moves(test_game["state"]) == test_game["moves"]
    
@pytest.mark.parametrize("test_game_index", range(N_TEST_GAMES))
def test_analyze(test_games, test_game_index):
    test_game = test_games[test_game_index]
    assert analyze(test_game["state"]) == test_game["win"]
    
@pytest.mark.parametrize("test_game_index", range(N_TEST_GAMES))
def test_state_from_file(input_files, test_games, test_game_index):
    test_file = input_files[test_game_index]
    result_state = state_from_file(str(test_file))
    assert result_state == test_games[test_game_index]["state"]
    

pytest.main(["P17_tictactoe_test.py", "-p", "no:faulthandler"])
