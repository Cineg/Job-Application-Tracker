from ..db.db import (
    TEST_DB_PATH,
    check_db_exists,
    create_db,
)

import os
import pytest


@pytest.fixture
def db_path() -> str:
    return TEST_DB_PATH


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
