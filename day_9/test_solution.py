import pytest
from pathlib import Path
from solution import part1


def test_part1_example():
    """Run part 1."""
    input_text = Path("example.txt")

    result = part1(input_text)
    assert result == 50

def test_part1_input():
    """Run part 1."""
    input_text = Path("input.txt")

    result = part1(input_text)
    assert result == 4758598740

# def test_example_part2():
#     input_text = Path("example.txt")
#     result = part2(input_text)
#     assert result == 40

# def test_part2_input():
#     input_text = Path("input.txt")

#     result = part2(input_text)
#     assert result == 348115621205535