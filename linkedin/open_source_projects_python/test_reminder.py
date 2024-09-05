# test_reminder.py

import reminder as app
from reminder import Task
import pytest
import datetime as dt


@pytest.fixture
def task_list() -> list:
    return [
        Task(name="pay rent"),
        Task(name="buy bread"),
    ]


def test_find_task():
    task_list = [
        Task(name="pay rent"),
        Task(name="buy bread"),
    ]

    expected = Task(name="buy bread")
    assert app._find_task("buy bread", task_list) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("buy bread", Task(name="buy bread")),
        ("buy banana", None),
    ],
)
def test_find_task_with_params(test_input, expected):
    task_list = [
        Task(name="pay rent"),
        Task(name="buy bread"),
    ]
    assert app._find_task(test_input, task_list) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("buy bread", Task(name="buy bread")),
        ("buy banana", None),
    ],
)
def test_find_task_with_fixture(test_input, expected, task_list):
    assert app._find_task(test_input, task_list) == expected


def test_to_date():
    expected = dt.date(2022, 9, 1)
    assert app._to_date("2022-09-01") == expected


def test_to_date_with_exceptions():
    with pytest.raises(ValueError) as e:
        _ = app._to_date("1234")


@pytest.mark.skip()
def test_skipping_a_test():
    expected = dt.date(2022, 9, 1)
    assert app._to_date("2022-09-01") == expected


@pytest.mark.xfail(reason="This will fail until we create the mock class.")
def test_expected_to_fail():
    _ = app._to_date("1234")
