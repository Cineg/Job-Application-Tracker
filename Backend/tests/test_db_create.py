from ..db.db import (
    TEST_DB_PATH,
    check_db_exists,
    create_db,
    create_offer_table,
    create_refresh_table,
    select_all,
    _get_timestamp,
)

import os
import pytest


@pytest.fixture
def db_path() -> str:
    return TEST_DB_PATH


# create db
def test_create_db_new(db_path: str) -> None:
    if os.path.exists(db_path):
        os.remove(db_path)

    res: bool = create_db(db_path)

    assert res is True


def test_create_db_exists(db_path: str) -> None:
    if not os.path.exists(db_path):
        create_db(db_path)

    res: bool = create_db(db_path)
    assert res is True


# db exist
def test_check_db_exists_invalid() -> None:
    res: bool = check_db_exists("ABC", False)
    assert res is False


def test_check_db_exists_create_db(db_path: str) -> None:
    res: bool = check_db_exists(db_path, True)
    assert res is True


def test_check_db_exitst_db_created(db_path: str) -> None:
    res: bool = check_db_exists(db_path, False)
    assert res is True


def test_check_db_exitst_db_recreate(db_path: str) -> None:
    res: bool = check_db_exists(db_path, True)
    assert res is True


# create_offer_table
def test_create_offer_table_db_not_existing(db_path: str) -> None:
    if os.path.exists(db_path):
        os.remove(db_path)

    res: bool = create_offer_table(db_path)
    assert res is False


def test_create_offer_table_db_exist(db_path: str) -> None:
    if os.path.exists(db_path):
        os.remove(db_path)

    if not os.path.exists(db_path):
        with open(db_path, "w"):
            pass

    res: bool = create_offer_table(db_path)
    data: list[list[str]] | None = select_all(db_path)

    assert res is True
    assert data is not None


# create_offer_table
def test_create_refresh_table_db_not_exist(db_path: str) -> None:
    if os.path.exists(db_path):
        os.remove(db_path)

    res: bool = create_refresh_table(db_path)
    assert res is False


def test_create_refresh_table_db_exist(db_path: str) -> None:
    if os.path.exists(db_path):
        os.remove(db_path)

    if not os.path.exists(db_path):
        with open(db_path, "w"):
            pass

    res: bool = create_refresh_table(db_path)
    data: str | None = _get_timestamp(db_path)

    assert res is True
    assert data is not None
