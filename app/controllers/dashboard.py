from flask import Blueprint, render_template, Response
from flask_login import login_required
from flask_login import current_user
from app.models.user import User
from datetime import date
from app.models.log import Log
from app.helpers.general_helper import drowsiness_detect

controller = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@controller.route('/', methods=['GET'])
@login_required
def index():
    if current_user.role == 'admin':
        total_users = User.query.filter(User.role == 'user').count()
        total_logs = Log.query.count()
        today_logs = Log.query.filter(Log.created_at == date.today()).count()
        return render_template('pages/dashboard/home_admin.jinja2', total_users=total_users, total_logs=total_logs,
                               today_logs=today_logs)
    else:
        return render_template('pages/dashboard/home_user.jinja2')


@controller.route('/video-stream', methods=['GET'])
@login_required
def video_stream():
    return Response(drowsiness_detect(current_user.get_id()), mimetype='multipart/x-mixed-replace; boundary=frame')
