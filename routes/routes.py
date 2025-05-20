from flask import Blueprint, render_template
from models import db
from models.user import User

questions_bp = Blueprint('questions', __name__)


@questions_bp.route('/army')
def questions_army():
    test_data = [
    {
        "title": "General Science",
        "questions": [
            {
                "question": "NaCl is more commonly known as:",
                "options": ["nickel chlorine", "pepper", "salt", "sugar"],
                "answer": "salt"
            }
        ]
    },
    {
        "title": "Arithmetic Reasoning",
        "questions": [
            {
                "question": "If there are three quarts of gas in a gallon container, how full is the container?",
                "options": ["50%", "60%", "75%", "80%"],
                "answer": "75%"
            }
        ]
    },
    
]
    return render_template('questions/army.html', test_data=test_data)

@questions_bp.route('/navy')
def questions_navy():
    return render_template('questions/navy.html')

@questions_bp.route('/air-force')
def questions_air_force():
    return render_template('questions/air-force.html')

@questions_bp.route('/military-health')
def questions_military_health():
    return render_template('questions/military-health.html')

@questions_bp.route('/computers')
def questions_computers():
    return render_template('questions/computers.html')
