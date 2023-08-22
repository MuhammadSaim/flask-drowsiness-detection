from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from app.models.user import User
from app.models.log import Log
from sqlalchemy import text
from flask_login import current_user
from app import db

controller = Blueprint('users', __name__, url_prefix='/dashboard/users')


@controller.route('/all', methods=['GET'])
@login_required
def all():
    if current_user.role != 'admin':
        return redirect(url_for('dashboard.index'))
    users = User.query.filter(User.role == 'user').order_by(text('users.id desc'))
    return render_template('pages/dashboard/users/all.jinja2', users=users)


@controller.route('/delete/<int:user_id>', methods=['GET'])
@login_required
def delete_user(user_id):
    if current_user.role != 'admin':
        return redirect(url_for('dashboard.index'))

    user = User.query.filter(User.id == user_id).first()

    if user is None:
        return redirect(url_for('users.all'))

    db.session.delete(user)
    db.session.flush()
    db.session.commit()
    return redirect(url_for('users.all'))


@controller.route('/<int:user_id>/logs', methods=['GET'])
@login_required
def user_logs(user_id):
    if current_user.role != 'admin':
        return redirect(url_for('dashboard.index'))

    user = User.query.filter(User.id == user_id).first()

    if user is None:
        return redirect(url_for('users.all'))

    logs = Log.query.filter(Log.user_id == user.id).order_by(text('logs.id desc'))
    return render_template("pages/dashboard/logs/all.jinja2", logs=logs)
