import pytest
from app.operations import Operations

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (2.5, 3.5, 6.0),
        (-1.5, -2.5, -4.0),
    ],
    ids=[
        "add_positive_integers",
        "add_negative_integers",
        "add_zero_integers",
        "add_positive_floats",
        "add_negative_floats"
    ]
)
def test_addition(a, b, expected):
    assert Operations.addition(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),
        (0, 1, -1),
        (-2, -3, 1),
        (2.5, 1.5, 1.0),
        (-1.5, -0.5, -1.0),
    ],
    ids=[
        "subtract_positive_integers",
        "subtract_zero_integers",
        "subtract_negative_integers",
        "subtract_positive_floats",
        "subtract_negative_floats"
    ]
)
def test_subtraction(a, b, expected):
    assert Operations.subtraction(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (-1, 1, -1),
        (0, 10, 0),
        (1.5, 2.0, 3.0),
        (-1.5, -2.0, 3.0),
    ],
    ids=[
        "multiply_positive_integers",
        "multiply_negative_integers",
        "multiply_zero_integers",
        "multiply_positive_floats",
        "multiply_negative_floats"
    ]
)
def test_multiplication(a, b, expected):
    assert Operations.multiplication(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2),
        (-4, 2, -2),
        (5.0, 2.5, 2.0),
        (-3.0, -1.5, 2.0),
    ],
    ids=[
        "divide_positive_integers",
        "divide_negative_integers",
        "divide_positive_floats",
        "divide_negative_floats"
    ]
)
def test_division(a, b, expected):
    assert Operations.division(a, b) == expected


@pytest.mark.parametrize(
    "a, b",
    [
        (1, 0),
        (0, 0),
        (-5, 0),
        (3.5, 0),
        (-2.0, 0),
    ],
    ids=[
        "divide_by_zero_positive_integers",
        "divide_by_zero_zero_integers",
        "divide_by_zero_negative_integers",
        "divide_by_zero_positive_floats",
        "divide_by_zero_negative_floats"
    ]
)
def test_division_by_zero(a, b):
    with pytest.raises(ValueError):
        Operations.division(a, b)