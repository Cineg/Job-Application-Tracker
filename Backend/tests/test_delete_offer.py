from flask import Response
from ..src.app import delete_offer, app

from ..db.db import TEST_DB_PATH, add_one_offer, _select_one
import json


def test_delete_offer_missing_arg() -> None:
    mock_data: dict[str, str] = {}

    with app.test_request_context(
        "/api/v1/update-offer",
        data=json.dumps(mock_data),
        method="PUT",
        content_type="application/json",
    ):
        res: Response = delete_offer(TEST_DB_PATH)

        assert res.status_code == 400


def test_delete_offer_not_existing_url() -> None:
    mock_data: dict[str, str] = {"url": "bleble"}

    with app.test_request_context(
        "/api/v1/update-offer",
        data=json.dumps(mock_data),
        method="PUT",
        content_type="application/json",
    ):
        res: Response = delete_offer(TEST_DB_PATH)

        assert res.status_code == 400


def test_delete_offer() -> None:
    mock_data: dict[str, str] = {"url": "a"}

    # ensure offer exists
    add_one_offer("a", "a", "a", TEST_DB_PATH)

    with app.test_request_context(
        "/api/v1/update-offer",
        data=json.dumps(mock_data),
        method="PUT",
        content_type="application/json",
    ):
        res: Response = delete_offer(TEST_DB_PATH)

        assert res.status_code == 200

    new_data: list[list[str]] | None = _select_one("a", TEST_DB_PATH)
    assert new_data is None
