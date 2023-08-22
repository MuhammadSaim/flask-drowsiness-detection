from flask import Flask, redirect, url_for
import config
from app import (
    db,
    migrate,
    login_manager,
    bcrypt,
    seeder
)
from app.models.user import User


def register_blueprints(app):
    from app.controllers import (
        home,
        auth,
        dashboard,
        users,
        log
    )

    app.register_blueprint(home.controller)
    app.register_blueprint(auth.controller)
    app.register_blueprint(dashboard.controller)
    app.register_blueprint(users.controller)
    app.register_blueprint(log.controller)


def initialize_plugins(app):
    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    seeder.init_app(app, db)


def import_models():
    # import database models
    from app.models import (
        user,
        log
    )


def import_helpers():
    from app.helpers.general_helper import (
        drowsiness_detect
    )


def initialize_flask_app():
    # Initialize the core application.
    app = Flask(
        __name__,
        instance_relative_config=False,
        template_folder=config.Config.TEMPLATES_FOLDER,
        static_folder=config.Config.STATIC_FOLDER,
        static_url_path=config.Config.STATIC_FOLDER_PATH
    )
    app.config.from_object('config.Config')

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @login_manager.unauthorized_handler
    def unauthorized_handler():
        return redirect(url_for('auth.login'))

    return app
