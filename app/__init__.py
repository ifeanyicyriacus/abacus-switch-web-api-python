from flask import Flask
from flask_cors import CORS

from app.calculator.calculator_controller import calculate_controller_bp

app = Flask(__name__)
CORS(app)

from app.calculator import calculator_controller
app.register_blueprint(calculate_controller_bp)
