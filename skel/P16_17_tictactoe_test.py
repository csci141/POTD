# POTD 16 17 test
import pytest
import pickle

from P16_17_tictactoe import *

N_TEST_GAMES = 7

@pytest.fixture(scope="module")
def test_games():
    with open("P16_17_test_data.pkl", "rb") as f:
        return pickle.loads(f.read())

@pytest.fixture(scope="module")
def input_files(tmp_path_factory, test_games):
    """
    Creates temporary files for all test cases and returns a mapping
    of test case index to file path. Uses module scope for reuse.
    """
    # Create a temporary directory for this module's tests
    tmp_dir = tmp_path_factory.mktemp("input_files")
    
    # Create a file for each test case
    file_mapping = {}
    for i, test_case in enumerate(test_games):
        test_file = tmp_dir / f"test_input_{i}.txt"
        test_file.write_text(test_case["input"])
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
    

pytest.main(["P16_17_tictactoe_test.py", "-vv", "--showlocals", "-p", "no:faulthandler"])
