import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from models import db
from models.user import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name= request.form['name'],
        email = request.form['email'],
        location = request.form['location'],
        interests = request.form['interests'],
        can_relocate = request.form.get('can_relocate') == '1' #only true or false
        username = request.form['username']
         
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                new_user = User(
                    name=name,
                    email=email,
                    location=location,
                    interests=interests,
                    can_relocate=can_relocate,
                    username=username,
                    password=generate_password_hash(password)
                )
                db.session.add(new_user)
                db.session.commit()
                flash('Registration successful. Please log in.')
                return redirect(url_for('auth.login'))
            except Exception as e:
                db.session.rollback()
                error = f"User {username} is already registered."
                print(f"Error: {error}")

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        # SQLAlchemy query to get the user by username
        user = User.query.filter_by(username=username).first()
        

        if user is None:
            error = 'Incorrect username.'

        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        if error is not None:
            flash(error)
            print(f"Login error: {error}")
        flash(error)

    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@bp.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out')
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
