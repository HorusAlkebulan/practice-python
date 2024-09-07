from number_placement import number_placement
import pytest


@pytest.mark.parametrize(
    argnames=["numbers", "operators", "expected"],
    argvalues=[
        ([], [], None),
        ([2], ["<"], None),
        ([2, 9], ["<"], "2 < 9"),
        ([2, 9], [">"], "9 > 2"),
        ([9, 7, 4, 3, 2], ["<", ">", "<", ">"], "2 < 9 > 3 < 7 > 4"),
    ],
)
def test_number_placement(numbers, operators, expected):
    print(f"numbers={numbers}, operators={operators}, expected={expected}")
    actual = number_placement(numbers, operators)
    assert actual == expected


if __name__ == "__main__":
    test_number_placement(numbers=[2, 9], operators=["<"], expected="2 < 9")
