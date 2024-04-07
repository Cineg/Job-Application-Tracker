from werkzeug.test import TestResponse
from ..src.app import add_offer, app
import json
from ..db.db import TEST_DB_PATH
from flask import Response


def test_add_offer_missing_key() -> None:
    mock_data: dict[str, str] = {"url": "zzz"}

    with app.test_request_context(
        "/api/v1/add-offer",
        method="POST",
        data=json.dumps(mock_data),
        content_type="application/json",
    ):

        res: Response = add_offer(TEST_DB_PATH)
        assert res.status_code == 400


def test_add_offer_invalid_key() -> None:
    mock_data: dict[str, str] = {"url": "zzz", "titlez": "blob", "company": "123"}

    with app.test_request_context(
        "/api/v1/add-offer",
        method="POST",
        data=json.dumps(mock_data),
        content_type="application/json",
    ):

        res: Response = add_offer(TEST_DB_PATH)
        assert res.status_code == 400


def test_add_offer() -> None:
    mock_data: dict[str, str] = {"url": "zzz", "title": "blob", "company": "123"}

    with app.test_request_context(
        "/api/v1/add-offer",
        method="POST",
        data=json.dumps(mock_data),
        content_type="application/json",
    ):

        res: Response = add_offer(TEST_DB_PATH)
        assert res.status_code == 200
