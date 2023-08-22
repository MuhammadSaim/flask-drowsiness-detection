from flask import Blueprint, redirect, url_for

controller = Blueprint('home', __name__)


@controller.route('/', methods=['GET'])
def index():
    return redirect(url_for('auth.login'))
