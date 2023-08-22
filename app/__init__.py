from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_seeder import FlaskSeeder

load_dotenv()

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()
seeder = FlaskSeeder()


def create_app():
    from app.settings import (
        initialize_flask_app,
        initialize_plugins,
        import_models,
        register_blueprints,
        import_helpers
    )
    app = initialize_flask_app()

    with app.app_context():
        # initialize plugins
        initialize_plugins(app)

        # register blueprints
        register_blueprints(app)

        # import models
        import_models()

        # import general helpers
        import_helpers()

        return app
