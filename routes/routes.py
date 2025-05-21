from flask import Blueprint, render_template
from models import db
from models.user import User

questions_bp = Blueprint('questions', __name__)


def get_department_data(department):
    sample_tests = {
        "army": [
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
            }
        ],
        "navy": [
            {
                "title": "Mechanical Comprehension",
                "questions": [
                    {
                        "question": "Which gear turns the opposite direction of gear A?",
                        "options": ["B", "C", "D", "E"],
                        "answer": "C"
                    }
                ]
            }
        ],
        "air-force": [],
        "military-health": [],
        "computers": []
    }
    return sample_tests.get(department, [])

@questions_bp.route('/<department>')
def questions_department(department):
    department_titles = {
        "army": "South African Army",
        "navy": "South African Navy",
        "air-force": "South African Air Force",
        "military-health": "Military Health Services",
        "computers": "Computer Aptitude"
    }

    application_links = {
        "army": "http://www.dod.mil.za/document/Form/Forms/SA%20Army%20MSDS%20Application%202026.pdf",
        "navy": "http://www.dod.mil.za/document/Form/Forms/SA%20Navy%20MSDS%20Application%202026.pdf",
        "air-force": "http://www.dod.mil.za/document/Form/Forms/SA%20AirForce%20MSDS%20Application%202026.pdf",
        "military-health": "http://www.dod.mil.za/document/Form/Forms/SA%20Health%20MSDS%20Application%202026.pdf",
        "computers": "http://www.dod.mil.za/document/Form/Forms/SA%20Computer%20MSDS%20Application%202026.pdf"
    }

    if department not in department_titles:
        return "Department not found", 404

    test_data = get_department_data(department)
    return render_template("questions/department.html",
                           department=department,
                           department_name=department_titles[department],
                           test_data=test_data,
                           application_link=application_links.get(department))

@questions_bp.route('/requirements/<branch>')
def requirements(branch):
    return render_template('questions/requirements.html', branch=branch)