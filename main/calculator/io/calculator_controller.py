from flask import Flask, jsonify, request
from flask_cors import CORS

from main.calculator.services.calculator import calculate

app = Flask(__name__)
CORS(app)


@app.route("/calculate", methods=['POST'])
def evaluate_expression():
    data: dict = request.get_json(force=True)
    # expression = data["expression"]
    expression = data.get('expression', "").strip()
    if expression == "":
        return jsonify({"error": "expression cannot be empty"})

    # print(expression)
    try:
        result = calculate(expression)
        return jsonify({"result": str(result)}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Calculation error"}), 500


# @app.route("/signUp", methods=['POST'])
# def sign_up():
#     data: dict = request.get_json(force=True)
#     response_dto: dict = data.pop("password")
#     return jsonify({
#         "firstName": response_dto.get("firstName"),
#         "lastName": response_dto.get("lastName"),
#         "email": response_dto.get("email"),
#     }),201

if __name__ == "__main__":
    app.run(debug=True)
