import os

from flask import Flask, jsonify, request
from flask_cors import CORS

from main.calculator.calculator import calculate

app = Flask(__name__)
CORS(app)


@app.route("/calculate", methods=['POST'])
def evaluate_expression():
    data: dict = request.get_json(force=True)
    # expression = data["expression"]
    expression = data.get('expression', "").strip()
    if expression == "":
        return jsonify({"error": "expression cannot be empty"})

    try:
        result = calculate(expression)
        return jsonify({"result": str(result)}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Calculation error"}), 500

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)