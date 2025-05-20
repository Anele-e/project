from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import user, db
from auth import bp as auth_bp
from routes.routes import questions_bp
from flask_migrate import Migrate

# Configure application

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # initialize the database
    db.init_app(app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(questions_bp, url_prefix='/questions')
    with app.app_context():
        db.create_all()
    return app
app = create_app()


    
migrate = Migrate(app, db)

@app.route('/')
def index():

    cards_data = [
        {
            "title": "South African Army",
            "image": "images/South_African_troops.jpg",
            "description": "Take an aptitude test",
            "link": url_for('questions.questions_army')
        },
        {
            "title": "South African Navy",
            "image": "images/navy.jpg",
            "description": "South African Navy",
            "link": url_for('questions.questions_navy') 
        },
        {
            "title": "South African Air Force",
            "image": "images/air-force.jpg",
            "description": "Get Random memes",
            "link": url_for('questions.questions_air_force') 
        },
        {
            "title": "South African Military Health Service",
            "image": "images/health-services.webp",
            "description": "There will be something here",
            "link": url_for('questions.questions_military_health') 
        },
        {
            "title": "Funuba kwi Computer",
            "image": "images/comp-image.jpg",
            "description": "Take aptitude test for computer skills",
            "link": url_for('questions.questions_computers') 
        },
        {
            "title": "Explore careers", 
            "image": "",
            "description": "There will be something here",
            "link": "#" 
        },
    ]
    return render_template('index.html', cards=cards_data)



if __name__ == '__main__':
    app.run(debug=True)




