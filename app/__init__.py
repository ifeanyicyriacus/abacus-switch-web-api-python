from flask import Flask
from flask_cors import CORS

from app.calculator.calculator_controller import calculate_controller_bp

app = Flask(__name__)
CORS(app, origins=[
    "https://abacus-switch-web-app-react-frontend.vercel.app/",
    "https://52.41.36.82",
    "https://54.191.253.12",
    "https://44.226.122.3",
    "http://localhost:5173"
])

from app.calculator import calculator_controller
app.register_blueprint(calculate_controller_bp)
