from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from app.models.log import Log
from sqlalchemy.sql import text

controller = Blueprint('log', __name__, url_prefix='/dashboard/logs')


@controller.route('/', methods=['GET'])
@login_required
def index():
    if current_user.role == 'admin':
        logs = Log.query.order_by(text('logs.id desc'))
    else:
        current_user_id = current_user.get_id()
        logs = Log.query.filter(Log.user_id==current_user_id).order_by(text('logs.id desc'))
    return render_template('pages/dashboard/logs/all.jinja2', logs=logs)

