# POTD 18 test
import pytest
from P18_morse import get_dictionary, reverse_dictionary, translate_fwd, translate_rev

@pytest.fixture
def sample_codebook_file(tmp_path):
    """Create a temporary morse code file for testing get_dictionary"""
    d = tmp_path / "morse"
    d.mkdir()
    p = d / "code.txt"
    p.write_text("""A .-
B -...
C -.-.
D -..
E .
1 .----
2 ..---""")
    return str(p)

@pytest.fixture
def morse_dict():
    """Full morse code dictionary from the provided sample file"""
    return {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        ' ': ''
    }

TRANSLATION_TEST_CASES = [
    ('ABC', '.- -... -.-.'),
    ('HELLO WORLD', '.... . .-.. .-.. ---  .-- --- .-. .-.. -..'),
    ('SOS', '... --- ...'),
    ('1234 5678 90', '.---- ..--- ...-- ....-  ..... -.... --... ---..  ----. -----'),
    ('TESTING 123', '- . ... - .. -. --.  .---- ..--- ...--'),
    ('A  B', '.-   -...'),  # Multiple spaces between letters
]

def test_get_dictionary(sample_codebook_file):
    """Test dictionary generation from code file"""
    expected = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        '1': '.----',
        '2': '..---',
        ' ': ''
    }
    
    result = get_dictionary(sample_codebook_file)
    assert result == expected
    assert ' ' in result  # Space character should be added automatically
    assert result[' '] == ''

def test_reverse_dictionary():
    """Test reverse dictionary generation"""
    input_dict = {
        'A': '.-',
        'B': '-...',
        ' ': ''
    }
    
    expected = {
        '.-': 'A',
        '-...': 'B',
        '': ' '
    }
    
    result = reverse_dictionary(input_dict)
    assert result == expected

@pytest.mark.parametrize("text,morse", TRANSLATION_TEST_CASES)
def test_translate_fwd(morse_dict, text, morse):
    """Test forward translation (text to morse)"""
    assert translate_fwd(morse_dict, text) == morse

@pytest.mark.parametrize("text,morse", TRANSLATION_TEST_CASES)
def test_translate_rev(morse_dict, text, morse):
    """Test reverse translation (morse to text)"""
    reverse_dict = reverse_dictionary(morse_dict)
    assert translate_rev(reverse_dict, morse) == text

def test_edge_cases(morse_dict):
    """Test various edge cases"""
    reverse_dict = reverse_dictionary(morse_dict)
    
    # Test empty dictionary
    empty_dict = {' ': ''}
    assert translate_fwd(empty_dict, 'ABC') == '? ? ?'
    
    # Test single character translations
    assert translate_fwd(morse_dict, 'A') == '.-'
    assert translate_rev(reverse_dict, '.-') == 'A'
    
    # Test mixed valid/invalid characters
    assert translate_fwd(morse_dict, 'A#B') == '.- ? -...'
    assert translate_rev(reverse_dict, '.- ? -...') == 'A?B'
    assert translate_rev(reverse_dict, '.- ? --.--') == 'A??'

pytest.main(["P18_morse_test.py",  "-vv", "--showlocals", "-p", "no:faulthandler", "-s"])
