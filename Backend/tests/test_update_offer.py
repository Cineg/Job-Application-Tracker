from flask import Response
from ..db.db import TEST_DB_PATH, add_one_offer, delete_offer, _select_one
from ..src.app import app, update_offer
import json


def test_update_offer_missing_arg() -> None:
    mock_data: dict[str, str] = {
        "url": "abc",
        "status": "abc",
        "company": "abc",
        "dateAdded": "abc",
    }

    with app.test_request_context(
        "/api/v1/update-offer",
        data=json.dumps(mock_data),
        method="PUT",
        content_type="application/json",
    ):
        res: Response = update_offer(TEST_DB_PATH)

        assert res.status_code == 400


def test_update_offer_incorrect_url() -> None:
    mock_data: dict[str, str] = {
        "url": "abc",
        "status": "abc",
        "company": "abc",
        "dateAdded": "abc",
        "title": "abc",
    }

    with app.test_request_context(
        "/api/v1/update-offer",
        data=json.dumps(mock_data),
        method="PUT",
        content_type="application/json",
    ):
        res: Response = update_offer(TEST_DB_PATH)

        assert res.status_code == 400


def test_update_offer() -> None:
    mock_data: dict[str, str] = {
        "url": "a",
        "status": "abc",
        "company": "abc",
        "dateAdded": "abc",
        "title": "BLOB",
    }

    # ensure correct offer is in db
    delete_offer("a", TEST_DB_PATH)
    add_one_offer("a", "abc", "abc", TEST_DB_PATH)

    with app.test_request_context(
        "/api/v1/update-offer",
        data=json.dumps(mock_data),
        method="PUT",
        content_type="application/json",
    ):
        res: Response = update_offer(TEST_DB_PATH)

        assert res.status_code == 200

    new_data: list[list[str]] | None = _select_one("a", TEST_DB_PATH)
    assert new_data is not None
    assert new_data[1][0][3] == "BLOB"
