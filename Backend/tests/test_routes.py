from ..src.app import app, routes
from flask import Response
from typing import Any
import json


def test_routes_status() -> None:
    with app.app_context():
        response: Response = routes()
        assert response.status_code == 200


def test_routes_value() -> None:
    with app.app_context():
        response: Response = routes()
        res: Any = json.loads(response.data.decode("utf-8"))

        assert type(res) is list

        for item in res:
            assert type(item) is str
