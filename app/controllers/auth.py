from flask import Blueprint, render_template, request, jsonify, url_for, redirect
from app.forms.login_form import LoginForm
from app.forms.register_form import RegisterForm
from app.helpers.general_helper import form_errors, is_ajax
from app.models.user import User
from app.settings import bcrypt
from app import db
from flask_login import login_user, logout_user, login_required, current_user

controller = Blueprint('auth', __name__, url_prefix='/auth')


@controller.route('/login', methods=['GET', 'POST'])
def login():
    print(current_user.get_id())
    if current_user.get_id() is not None:
        return redirect(url_for('dashboard.index'))
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit() and is_ajax(request):
            username = form.username.data
            password = form.password.data

            user = User.query.filter_by(username=username).first()

            if not user or not bcrypt.check_password_hash(user.password, password):
                return jsonify({
                    'error': True,
                    'form': True,
                    'messages': {
                        'username': 'Username/password is incorrect.'
                    }
                })

            login_user(user, remember=True)
            return jsonify({
                'error': False,
                'redirect_url': url_for('dashboard.index', _external=True),
                'messages': 'You are successfully login.'
            })

        else:
            return jsonify({
                'error': True,
                'form': True,
                'messages': form_errors(form)
            })
    return render_template('pages/auth/login.jinja2', form=form)


@controller.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.get_id() is not None:
        return redirect(url_for('dashboard.index'))
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit() and is_ajax(request):
            name = form.name.data
            username = form.username.data
            email = form.email.data
            password = form.password.data
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = User()
            user.name = name
            user.username = username
            user.email = email
            user.password = hashed_password
            db.session.add(user)
            db.session.flush()
            db.session.commit()
            return jsonify({
                'error': False,
                'redirect_url': url_for('auth.login', _external=True),
                'messages': 'You are registered successfully.'
            })
        else:
            return jsonify({
                'error': True,
                'form': True,
                'messages': form_errors(form)
            })
    return render_template("pages/auth/register.jinja2", form=form)


@controller.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
