# POTD 19 test
import pytest

from P19_sieve import get_factors

def test_basic_functionality():
    """Test basic functionality with a small number"""
    result = get_factors(4)
    expected = {
        2: [1, 2],
        3: [1, 3],
        4: [1, 2, 4]
    }
    assert result == expected

def test_minimum_input():
    """Test with minimum valid input N=2"""
    result = get_factors(2)
    expected = {2: [1, 2]}
    assert result == expected

def test_prime_number():
    """Test with a prime number to ensure only 1 and itself are factors"""
    result = get_factors(7)
    assert result[7] == [1, 7]

def test_highly_composite():
    """Test with a number that has many factors"""
    result = get_factors(12)
    assert result[12] == [1, 2, 3, 4, 6, 12]

def test_consecutive_numbers():
    """Test that all numbers between 2 and N are present as keys"""
    n = 6
    result = get_factors(n)
    assert set(result.keys()) == set(range(2, n+1))

def test_factors_are_ordered():
    """Test that factors are listed in ascending order"""
    result = get_factors(8)
    for factors in result.values():
        assert factors == sorted(factors)

def test_all_lists_start_with_one():
    """Test that every number's factor list starts with 1"""
    result = get_factors(10)
    for factors in result.values():
        assert factors[0] == 1

def test_factors_are_valid():
    """Test that all listed factors actually divide their number"""
    result = get_factors(9)
    for num, factors in result.items():
        for factor in factors:
            assert num % factor == 0

@pytest.mark.parametrize("n,m,expected", [
    (6, 4, [1, 2, 4]),
    (8, 6, [1, 2, 3, 6]),
    (10, 8, [1, 2, 4, 8]),
    (10000, 9876, [1, 2, 3, 4, 6, 12, 823, 1646, 2469, 3292, 4938, 9876]),
])

def test_specific_numbers(n, m, expected):
    """Test specific number combinations"""
    result = get_factors(n)
    assert result[m] == expected

pytest.main(["P19_sieve_test.py", "-p", "no:faulthandler", "-vv", "-s", "--showlocals"])
