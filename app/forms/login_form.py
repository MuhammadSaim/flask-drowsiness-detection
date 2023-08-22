from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, DataRequired
from app.validators.username_exists import UsernameExists


class LoginForm(FlaskForm):
    username = StringField(
        'username',
        validators=[InputRequired(), DataRequired(), UsernameExists(login=True)],
        render_kw={
            'class': 'input input-bordered w-full focus:outline-2 focus:outline-blue-700',
            'placeholder': 'Username'
        }
    )
    password = PasswordField(
        'password',
        validators=[InputRequired(), DataRequired()],
        render_kw={
            'class': 'input input-bordered w-full focus:outline-2 focus:outline-blue-700',
            'placeholder': 'Password'
        }
    )