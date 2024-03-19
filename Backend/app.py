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
        "POST   /api/v1/update-offer",
        "DELETE /api/v1/delete-offer",
    ]
    return jsonify(routes)


@app.route("/api/v1/results", methods=["GET"])
def results() -> Response:
    results: list[list[str]] | None = db.select_all()
    if results == None:
        return jsonify({"Message": "No results"})

    result: dict[str, list[dict]] = parse_db_query(results)

    return jsonify(result)


@app.route("/api/v1/add-offer", methods=["POST"])
def add_offer() -> Response:
    data: dict[str, str] = request.form

    for key in ["url", "company", "title"]:
        if key not in data:
            return Response(f"{key.capitalize()} not provided", 400)
        elif type(data[key]) != str:
            return Response(f"{key.capitalize()} - not acceptable datatype", 400)
        elif data[key] == "":
            return Response(f"{key.capitalize()} value not provided", 400)

    if not db.add_one_offer(data["url"], data["company"], data["title"]):
        return Response("Can't add data to database. Please try again.", 400)

    return jsonify(success=True)


@app.route("/api/v1/update-offer", methods=["PUT"])
def update_offer() -> Response:
    data: dict[str, str] = request.form
    for key in ["url", "status"]:
        if key not in data:
            return Response(f"{key.capitalize()} not provided", 400)
        elif type(data[key]) != str:
            return Response(f"{key.capitalize()} - not acceptable datatype", 400)
        elif data[key] == "":
            return Response(f"{key.capitalize()} value not provided", 400)

    if not db.update_status(data["url"], data["status"]):
        return Response("Can't update database. Please try again.", 400)

    return jsonify(success=True)


@app.route("/api/v1/delete-offer", methods=["DELETE"])
def delete_offer() -> Response:
    data: dict[str, str] = request.form
    for key in ["url"]:
        if key not in data:
            return Response(f"{key.capitalize()} not provided", 400)
        elif type(data[key]) != str:
            return Response(f"{key.capitalize()} - not acceptable datatype", 400)
        elif data[key] == "":
            return Response(f"{key.capitalize()} value not provided", 400)

    if not db.delete_offer(data["url"]):
        return Response("Can't delete item from database. Please try again.", 400)

    return jsonify(success=True)
