from flask import Flask, request, jsonify, Response

from typing import List, Dict
from utils import transform
from file_path import get_file_path

app = Flask(__name__)


@app.route("/perform_query", methods=['POST'])
def perform_query() -> Response:
    req_json: Dict[str, str] = request.json
    file_name: str = req_json["file_name"]
    cmd1: str = req_json["cmd1"]
    value1: str = req_json["value1"]
    cmd2: str = req_json["cmd2"]
    value2: str = req_json["value2"]

    file_data: List[str] = get_file_path(file_name=file_name)

    filter1: List[str] = transform(func=cmd1, value=value1, file_data=file_data)
    filter2: List[str] = transform(func=cmd2, value=value2, file_data=filter1)

    return jsonify(filter2)


if __name__ == "__main__":
    app.run()
