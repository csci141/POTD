# POTD 16 test
import os
import pytest
import pathlib

from P16_rle import encode_rle, decode_rle

0.6666666666666666
0.8153846153846154
0.5975103734439834
0.6268656716417911
2.0
1.0239234449760766


test_cases = [
    {"input": """\
██   ████""",
     "encoded": """\
2█3 4█""",
    "ratio": 0.6666666666666666},
    {"input": """\
    ██████    
  ██      ██  
 █          █ 
█  ██    ██  █
█            █
█  █      █  █
 █  ██████  █ 
  ██      ██  
    ██████""",
     "encoded": """\
4 6█4 
2 2█6 2█2 
1 1█10 1█1 
1█2 2█4 2█2 1█
1█12 1█
1█2 1█6 1█2 1█
1 1█2 6█2 1█1 
2 2█6 2█2 
4 6█""",
    "ratio": 0.8153846153846154},
    {"input": """\
    █████  █████    
  ██     ██     ██  
 █               █  
 █               █  
  █             █   
   █           █    
    █         █     
     █       █      
      █     █       
       █   █        
        █ █         
         █""",
     "encoded": """\
4 5█2 5█4 
2 2█5 2█5 2█2 
1 1█15 1█2 
1 1█15 1█2 
2 1█13 1█3 
3 1█11 1█4 
4 1█9 1█5 
5 1█7 1█6 
6 1█5 1█7 
7 1█3 1█8 
8 1█1 1█9 
9 1█""",
    "ratio": 0.5975103734439834},
    {"input": """\
       █        
      █ █       
     █   █      
    █     █     
   █████████    
  █         █   
 █           █  
█             █""",
     "encoded": """\
7 1█8 
6 1█1 1█7 
5 1█3 1█6 
4 1█5 1█5 
3 9█4 
2 1█9 1█3 
1 1█11 1█2 
1█13 1█""",
    "ratio": 0.6268656716417911},
    {"input": """\
█ █ █ █ █ █ █ █ 
 █ █ █ █ █ █ █ █
█ █ █ █ █ █ █ █ 
 █ █ █ █ █ █ █ █
█ █ █ █ █ █ █ █ 
 █ █ █ █ █ █ █ █
█ █ █ █ █ █ █ █ 
 █ █ █ █ █ █ █ █""",
     "encoded": """\
1█1 1█1 1█1 1█1 1█1 1█1 1█1 1█1 
1 1█1 1█1 1█1 1█1 1█1 1█1 1█1 1█
1█1 1█1 1█1 1█1 1█1 1█1 1█1 1█1 
1 1█1 1█1 1█1 1█1 1█1 1█1 1█1 1█
1█1 1█1 1█1 1█1 1█1 1█1 1█1 1█1 
1 1█1 1█1 1█1 1█1 1█1 1█1 1█1 1█
1█1 1█1 1█1 1█1 1█1 1█1 1█1 1█1 
1 1█1 1█1 1█1 1█1 1█1 1█1 1█1 1█""",
    "ratio": 2.0},
    {"input": """\
█    █   ██████ █ ██
█  █ ██ █████  █    
█ ███ █  █ ██  ███ █
 ██ █████ █  █ █ ███
█  ██  ██  █████ █ █
 █    ████ █  █ ███ 
█ █ ████  █     ██  
   █  ██ ██ ████████
       █  ████ █ ██ 
█████       ██     █""",
     "encoded": """\
1█4 1█3 6█1 1█1 2█
1█2 1█1 2█1 5█2 1█4 
1█1 3█1 1█2 1█1 2█2 3█1 1█
1 2█1 5█1 1█2 1█1 1█1 3█
1█2 2█2 2█2 5█1 1█1 1█
1 1█4 4█1 1█2 1█1 3█1 
1█1 1█1 4█2 1█5 2█2 
3 1█2 2█1 2█1 8█
7 1█2 4█1 1█1 2█1 
5█7 2█5 1█""",
    "ratio": 1.0239234449760766}
]

img_dir = pathlib.Path("./P16_img")

@pytest.fixture(scope="module")
def input_files():
    """
    Creates files for all test cases and returns a mapping
    of test case index to file path. Uses module scope for reuse.
    """
    img_dir.mkdir(exist_ok=True)
    
    # Create a file for each test case
    file_mapping = {}
    for i in range(len(test_cases)):
        raw_file = img_dir / f"P16_img{i}_raw.txt"
        enc_file = img_dir / f"P16_img{i}_rle.txt"
        
        raw_file.write_text(test_cases[i]["input"])
        enc_file.write_text(test_cases[i]["encoded"])
        file_mapping[i] = {"raw": raw_file, "enc": enc_file}
    
    return file_mapping


@pytest.mark.parametrize("test_image_index", range(6))
def test_rle_encode(input_files, test_image_index):
    input_file = input_files[test_image_index]["raw"]
    encoded_file = img_dir / f"P16_img{test_image_index}_enc_out.txt"
    
    calculated_ratio = encode_rle(input_file, encoded_file)
    
    result = encoded_file.read_text().rstrip('\n')
    assert result == test_cases[test_image_index]["encoded"]

    expected_ratio = test_cases[test_image_index]["ratio"]
    assert pytest.approx(expected_ratio) == calculated_ratio

@pytest.mark.parametrize("test_image_index", range(6))
def test_rle_decode(input_files, test_image_index):
    encoded_file = input_files[test_image_index]["enc"]
    decoded_file = img_dir / f"P16_img{test_image_index}_dec_out.txt"
    
    decode_rle(encoded_file, decoded_file)
    result = decoded_file.read_text().rstrip('\n')
    
    assert result == test_cases[test_image_index]["input"]

@pytest.mark.parametrize("test_image_index", range(6))
def test_end_to_end(input_files, test_image_index):
    input_file = input_files[test_image_index]["raw"]  
    encoded_file = pathlib.Path(f"P16_img/P16_img{test_image_index}_e2e_enc.txt")
    decoded_file = pathlib.Path(f"P16_img/P16_img{test_image_index}_e2e_dec.txt")
    
    encode_rle(input_file, encoded_file)
    decode_rle(encoded_file, decoded_file)

    result = decoded_file.read_text().rstrip('\n')
    assert result == test_cases[test_image_index]["input"]

if __name__ == "__main__":
    pytest.main(["P16_rle_test.py", "-vv", "-p", "no:faulthandler"])

