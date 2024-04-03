import json
from typing import Any

from flask import Response
from app import routes, results, app


def test_routes_status() -> None:
    with app.app_context():
        response: Response = routes()
        res: Any = json.loads(response.data.decode("utf-8"))

        assert response.status_code == 200


def test_routes_value() -> None:
    with app.app_context():
        response: Response = routes()
        res: Any = json.loads(response.data.decode("utf-8"))

        assert type(res) is list

        for item in res:
            assert type(item) is str


def test_results_status() -> None:
    with app.app_context():
        response: Response = results()

        assert response.status_code == 200


def test_results_value() -> None:
    with app.app_context():
        response: Response = results()
        res: Any = json.loads(response.data.decode("utf-8"))

        assert type(res) is dict


def test_results_keys() -> None:
    with app.app_context():
        response: Response = results()
        res: Any = json.loads(response.data.decode("utf-8"))

        for offer in res["Offers"]:
            assert "url" in offer.keys()
            assert "company" in offer.keys()
            assert "title" in offer.keys()
            assert "status" in offer.keys()
            assert "dateAdded" in offer.keys()
