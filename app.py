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

#     SA Army
# SA Air Force
# SA Navy
# SA Military Health Service

    cards = [
        {
            "title": "South African Army",
            "image": "images/South_African_troops.jpg",
            "description": "Take an aptitude test",
            "link": "https://www.army.mil.za/Recruitment/index.html"
        },
        {
            "title": "South African Navy",
            "image": "images/navy.jpg",
            "description": "South African Navy",
            "link": "https://www.navy.mil.za/Recruitment/index.html"
        },
         {
            "title": "South African Air Force",
            "image": "images/air-force.jpg",
            "description": "Get Random memes"
        },
        {
            "title": "South African Military Health Service",
            "image": "images/health-services.webp",
            "description": "There will be something here"
        },
          {
            "title": "Funuba kwi Computer",
            "image": "images/comp-image.jpg",
            "description": "Take aptitude test for computer skills"
        },
        {
            "title": "Explore careers",
            "image": "",
            "description": "There will be something here"
        },
    ]
    return render_template('index.html', cards=cards)



if __name__ == '__main__':
    app.run(debug=True)




