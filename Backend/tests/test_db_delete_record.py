import os
import pytest
from datetime import date, timedelta

from ..db.db import TEST_DB_PATH, delete_offer, create_db, add_one_offer, _select_one


@pytest.fixture
def db_path() -> str:
    if not os.path.exists(TEST_DB_PATH):
        create_db(TEST_DB_PATH)

    return TEST_DB_PATH


@pytest.fixture
def db_not_existing() -> str:
    return "blob.db"


def test_delete_record_not_existing_db(db_not_existing: str) -> None:
    assert delete_offer("A", db_not_existing) is False
    assert os.path.exists(db_not_existing) is False


def test_delete_record_record_not_exist(db_path: str) -> None:
    url: str = "ASDFASD"
    assert delete_offer(url, db_path) is False


def test_delete_record(db_path: str) -> None:
    url: str = "ABC"
    company: str = "yes"
    title: str = "Magician"

    add_one_offer(url, company, title, db_path)
    assert delete_offer(url, db_path) is True
    assert _select_one(url, db_path) is None
