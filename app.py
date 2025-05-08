from flask import Flask, flash, redirect, render_template, request, session
# from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import user, db
from auth import bp as auth_bp
from flask_migrate import Migrate

# Configure application



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # initialize the database
    db.init_app(app)



    
    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()
    return app
app = create_app()
migrate = Migrate(app, db)

@app.route('/')
def index():
    # sample data for cards in the index page
    cards = [
        {
            "title": "amajoni",
            "image": "images/South_African_troops.jpg",
            "description": "Take an aptitude test"
        },
        {
            "title": "Funuba kwi Computer",
            "image": "images/comp-image.jpg",
            "description": "Take aptitude test for computer skills"
        },
        {
            "title": "Results",
            "image": "images/wheret.jpg",
            "description": "Calculate where you can be placed"
        },
         {
            "title": "api memes",
            "image": "",
            "description": "Get Random memes"
        },
        {
            "title": "Blank1",
            "image": "",
            "description": "There will be something here"
        },
        {
            "title": "Blank2",
            "image": "",
            "description": "There will be something here"
        },
    ]
    return render_template('index.html', cards=cards)

def get_these_memes():
    url = f"https://api.memegen.link" #????????????


if __name__ == '__main__':
    app.run(debug=True)




