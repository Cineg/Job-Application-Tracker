import os
import pytest
from datetime import date

from ..db.db import TEST_DB_PATH, add_one_offer, _add_timestamp, _get_timestamp


@pytest.fixture
def db_path() -> str:
    return TEST_DB_PATH


def test_add_one_offer(db_path: str) -> None:
    if os.path.exists(db_path):
        os.remove(db_path)

    res: bool = add_one_offer("a", "b", "c", db_path)
    assert res is True


def test_add_one_offer_duplicate(db_path: str) -> None:
    if os.path.exists(db_path):
        os.remove(db_path)

    add_one_offer("a", "b", "c", db_path)
    res: bool = add_one_offer("a", "b", "c", db_path)

    assert res is False


def test__add_timestamp(db_path: str) -> None:
    assert _add_timestamp(db_path) is True


def test__add_timestamp_db_not_exist(db_path: str) -> None:
    if os.path.exists(db_path):
        os.remove(db_path)

    assert _add_timestamp(db_path) is True


def test__add_timestamp_date(db_path: str) -> None:
    if os.path.exists(db_path):
        os.remove(db_path)

    res: bool = _add_timestamp(db_path)
    stamp: str | None = _get_timestamp(db_path)

    today_date: str = date.today().strftime("%Y-%m-%d")

    assert res is True
    assert stamp is not None
    assert (stamp == today_date) is True
