from flask import jsonify, request, Blueprint
from app.calculator.calculator import calculate

calculate_controller_bp = Blueprint("calculate_controller_bp", __name__)


@calculate_controller_bp.route("/calculate", methods=["POST"])
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
