import pytest
from pathlib import Path
from solution import parse_input, part1, part2


@pytest.fixture
def input_data():
    """Load and parse the input file."""
    input_text = Path("input.txt").read_text()
    return parse_input(input_text)


def test_part1(input_data):
    """Run part 1."""
    result = part1(input_data)
    print(f"\nPart 1: {result}")
    # assert result == expected_value  # Uncomment when you know the answer


def test_part2(input_data):
    """Run part 2."""
    result = part2(input_data)
    print(f"\nPart 2: {result}")
    # assert result == expected_value  # Uncomment when you know the answer