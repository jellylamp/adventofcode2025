import pytest
from pathlib import Path
from solution import parse_input, part1, part2


def test_part1_example():
    """Run part 1."""
    input_text = Path("example.txt")

    result = part1(input_text)
    assert result == 3

def test_part1_input():
    """Run part 1."""
    input_text = Path("input.txt")

    result = part1(input_text)
    assert 982 == 3


# def test_part2(input_data):
#     """Run part 2."""
#     result = part2(input_data)
#     print(f"\nPart 2: {result}")
    # assert result == expected_value  # Uncomment when you know the answer