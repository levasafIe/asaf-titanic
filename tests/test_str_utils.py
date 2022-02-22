# Filename has to start with "test_"
import pytest

import hypothesis.strategies as st
from hypothesis import given

from titanic_utils.str_utils import extract_titles


# @ = "Decorators"
@pytest.mark.parametrize(
    "expected_input, expected_output",
    [
        ("Mr. John Doe", "Mr."),
        ("Miss. Jane Doe", "Miss."),
        ("Dr. Manhattan", "Dr."),
        # ("Mr.Juan Luis", "Mr."),  # Fails!
        # ("Mr Juan Luis", "Mr."),  # Fails!
    ],
)
def test_extract_titles_returns_expected_output(expected_input, expected_output):
    # 2. Run the code
    output = extract_titles(expected_input)

    # 3. Verify
    assert output == expected_output
    assert output[-1] == "."


def test_extract_titles_simple_input():
    assert extract_titles("Mr. John Doe") == "Mr."


def test_extract_titles_without_dot_raises_error():
    with pytest.raises(ValueError):
        extract_titles("Alabama")


@given(st.text(alphabet=st.characters(blacklist_characters=["."])))
def test_extract_titles_with_gibberish_without_dots_raises_error(input_text):
    with pytest.raises(ValueError):
        extract_titles(input_text)
