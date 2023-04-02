from flask import Flask, request, jsonify
from flask_restx import Resource, Namespace, Api

from utils import transform
from file_path import get_file_path

app = Flask(__name__)
api = Api(app)

perform_query_ns = Namespace("perform_query")
api.add_namespace(perform_query_ns)


@perform_query_ns.route('/')
class PerformQuery(Resource):
    def post(self):
        req_json = request.json
        file_name = req_json["file_name"]
        cmd1 = req_json["cmd1"]
        value1 = req_json["value1"]
        cmd2 = req_json["cmd2"]
        value2 = req_json["value2"]

        file_data = get_file_path(file_name=file_name)

        result = transform(func=cmd1, value=value1, file_data=file_data)
        result = transform(func=cmd2, value=value2, file_data=result)

        return jsonify(result)


if __name__ == "__main__":
    app.run()
