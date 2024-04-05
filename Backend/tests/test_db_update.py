import os
import pytest
from datetime import date, timedelta

from ..db.db import (
    TEST_DB_PATH,
    update_status,
    _update_timestamp,
    _update_statuses,
    _get_timestamp,
    add_one_offer,
    _select_one,
    create_db,
    delete_offer,
)


@pytest.fixture
def db_path() -> str:
    if not os.path.exists(TEST_DB_PATH):
        create_db(TEST_DB_PATH)

    return TEST_DB_PATH


@pytest.fixture
def db_not_existing() -> str:
    return "blob.db"


def test_update_status_db_doesnt_exist(db_not_existing: str) -> None:
    res: bool = update_status("A", "B", "C", "D", "SAD", db_not_existing)
    assert res is False
    assert os.path.exists(db_not_existing) is False


def test_update_status_item_doesnt_exist(db_path: str) -> None:
    res: bool = update_status("A", "B", "C", "D", "SAD", db_path)
    assert res is False


def test_update_status_item_exist(db_path: str) -> None:
    url: str = "A"
    company: str = "B"
    title: str = "C"

    add_one_offer(url, company, title, db_path)

    res: bool = update_status(
        url, "NEW_STATUS", "NEW_TITLE", "NEW_DATE", "NEW_COMPANY", db_path
    )
    data: list[list[str]] | None = _select_one(url, db_path)

    assert res is True
    assert data is not None
    assert data[1][0][1] == url
    assert data[1][0][2] == "NEW_COMPANY"
    assert data[1][0][3] == "NEW_TITLE"
    assert data[1][0][4] == "NEW_STATUS"
    assert data[1][0][5] == "NEW_DATE"


def test_update_timestamp_db_not_exist(db_not_existing: str) -> None:
    assert _update_timestamp(db_not_existing) is False
    assert os.path.exists(db_not_existing) is False


def test_update_timestamp(db_path: str) -> None:
    new_time: date = date.today() + timedelta(-35)
    new_time_str: str = new_time.strftime("%Y-%m-%d")

    res: bool = _update_timestamp(db_path, new_time)
    timestamp: str | None = _get_timestamp(db_path)

    assert res is True
    assert timestamp is not None

    assert new_time_str == timestamp


def test_update_statuses_no_db(db_not_existing: str) -> None:
    assert _update_statuses(db_path=db_not_existing) is False
    assert os.path.exists(db_not_existing) is False


def test_update_statuses_one_not_existing(db_path: str) -> None:
    new_time: date = date.today() + timedelta(-35)
    _update_timestamp(db_path, new_time)

    assert _update_statuses("SAIDHJASI", db_path) is False


def test_update_statuses_one_no_change(db_path: str) -> None:
    new_time: date = date.today() + timedelta(-25)
    _update_timestamp(db_path, new_time)

    url: str = "A"
    company: str = "B"
    title: str = "C"

    delete_offer(url, db_path)
    add_one_offer(url, company, title, db_path)
    res: list[list[str]] | None = _select_one(url, db_path)

    assert _update_statuses(url, db_path) is True
    assert res is not None
    assert res[1][0][4] == "Applied"


def test_update_statuses_one_change(db_path: str) -> None:
    new_time: date = date.today() + timedelta(-35)
    new_time_str = new_time.strftime("%Y-%m-%d")

    url: str = "A"
    company: str = "B"
    title: str = "C"

    delete_offer(url, db_path)
    add_one_offer(url, company, title, db_path)
    update_status(url, "Applied", title, new_time_str, company, db_path)
    _update_timestamp(db_path)

    assert _update_statuses(url, db_path, False) is True

    res: list[list[str]] | None = _select_one(url, db_path)
    assert res is not None
    assert res[1][0][4] != "Applied"
