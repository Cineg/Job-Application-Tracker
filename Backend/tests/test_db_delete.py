from ..db.db import delete_local_db, TEST_DB_PATH, create_db
import pytest
import os


@pytest.fixture
def db_path() -> str:
    return TEST_DB_PATH


def test_delete_not_existing_path() -> None:
    res: bool = delete_local_db("ABC")
    assert res is False


def test_delete_db(db_path: str) -> None:
    if not os.path.exists(db_path):
        create_db(db_path)

    res: bool = delete_local_db(db_path)
    assert res is True
    assert os.path.exists(db_path) is False
