from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from models.user import User

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        location = request.form['location']
        gpa = float(request.form['gpa']) if request.form['gpa'] else None
        interests = request.form['interests']
        user = User(name=name, email=email, location=location, gpa=gpa, interests=interests)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('profile.view_profile', user_id=user.id))
    return render_template('profile.html')

@profile_bp.route('/profile/<int:user_id>')
def view_profile(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('profile.html', user=user)
