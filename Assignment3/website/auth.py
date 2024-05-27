from flask import Blueprint, flash, render_template, url_for, redirect
from .forms import LoginForm, RegisterForm

from flask_login import login_user, login_required, logout_user
from flask_bcrypt import generate_password_hash, check_password_hash
from .models import User
from . import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    register = RegisterForm()
    if(register.validate_on_submit()==True):
        user_name = register.user_name.data
        email = register.email_id.data
        password = register.password.data
        user = db.session.scalar(db.select(User).where(User.username==user_name))
        if user:
            flash('Username already exists')
            return redirect(url_for('auth.register'))
        hashed_password = generate_password_hash(password)
        new_user = User(username=user_name, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('main.index'))
    else:
        return render_template('user.html', form=register, heading='Register')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    error = None
    if(login_form.validate_on_submit()==True):
        user_name = login_form.user_name.data
        password = login_form.password.data
        user = db.session.scalar(db.select(User).where(User.username == user_name))
        if user is None:
            error = 'Incorrect username'
        elif not check_password_hash(user.password_hash, password):
            error = 'Incorrect password'
        if error is None:
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash(error)
    return render_template('user.html', form=login_form, heading='Login')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
