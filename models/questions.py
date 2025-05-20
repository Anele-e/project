from models import db
from enum import Enum

#will have apis to interact with my databases

# Scrape tests from the web and store them in a database
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(100), nullable=False)
    options = db.Column(db.JSON, nullable=False)
    correct_answer = db.Column(db.String(200), nullable=False)
    explaination = db.Column(db.String(120), unique=True, nullable=False)
    category = db.Column(
        Enum('Numerical', 'Verbal', 'Spatial', '', name='reasoning_category'),
        nullable=False
    )
    difficulty_level = db.Column(
        Enum('easy', 'medium', 'hard', name='difficulty_enum'),
        nullable=False
    )
    relevant_department = db.Column(
        Enum('Navy', 'Army', 'Air Force', 'Health', name='difficulty_enum'),
        nullable=False
    )



