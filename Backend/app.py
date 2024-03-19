from flask import Flask, Response, jsonify, request
from flask_cors import CORS

from db_parser import parse_db_query
from db import db

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
@app.route("/api/", methods=["GET"])
@app.route("/api/v1/", methods=["GET"])
def routes() -> Response:
    routes: list[str] = [
        "GET    /api/v1/",
        "GET    /api/v1/results",
        "POST   /api/v1/add-offer",
    ]
    return jsonify(routes)


@app.route("/api/v1/results", methods=["GET"])
def results() -> Response:
    results: list[list[str]] | None = db.select_all()
    if results == None:
        return jsonify({"Message": "No results"})

    result: dict[str, list[dict]] = parse_db_query(results)
    print(result)
    return jsonify(result)


@app.route("/api/v1/add-offer", methods=["POST"])
def add_offer():
    data: dict[str, str] = request.form

    for key in ["url", "company", "title"]:
        if key not in data:
            return f"{key.capitalize()} not provided", 400
        if type(data[key]) != str:
            return f"{key.capitalize()} - not acceptable datatype", 400
        if data[key] == "":
            return f"{key.capitalize()} value not provided", 400

        db.add_one_offer(data["url"], data["company"], data["title"])

    return jsonify(success=True)
