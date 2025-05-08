from flask import Flask, flash, redirect, render_template, request, session
# from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import user, db
from auth import bp as auth_bp

# Configure application



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # initialize the database
    db.init_app(app)



    import auth
    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()
    return app
app = create_app()

@app.route('/')
def index():
    # sample data for cards in the index page
    cards = [
        {
            "title": "ijoni",
            "image": "images/South_African_troops.jpg",
            "description": "Take an aptitude test if you want to become a soldier"
        },
        {
            "title": "Funuba kwi Computer",
            "image": "images/icons8-bash-48.png",
            "description": "Learn about computer careers"
        },
        {
            "title": "Eze zandla",
            "image": "images/icons8-bash-48.png",
            "description": "Vocational training"
        },
    ]
    return render_template('index.html', cards=cards)

if __name__ == '__main__':
    app.run(debug=True)




