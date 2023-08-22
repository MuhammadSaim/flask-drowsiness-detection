from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import InputRequired, DataRequired, Email, EqualTo, Length, Regexp
from app.validators.username_exists import UsernameExists
from app.validators.email_exists import EmailExists


class RegisterForm(FlaskForm):
    name = StringField(
        'name',
        validators=[InputRequired(), DataRequired()],
        render_kw={
            'class': 'input input-bordered w-full focus:outline-2 focus:outline-blue-700',
            'placeholder': 'Name'
        }
    )
    username = StringField(
        'username',
        validators=[InputRequired(), DataRequired(), Regexp('^[a-zA-Z_0-9]\w+$', message="Only alphabets, numbers and _ are allowed."), UsernameExists()],
        render_kw={
            'class': 'input input-bordered w-full focus:outline-2 focus:outline-blue-700',
            'placeholder': 'Username'
        }
    )
    email = EmailField(
        'email',
        validators=[InputRequired(), DataRequired(), Email(), EmailExists()],
        render_kw={
            'class': 'input input-bordered w-full focus:outline-2 focus:outline-blue-700',
            'placeholder': 'Email'
        }
    )
    password = PasswordField(
        'password',
        validators=[InputRequired(), DataRequired(), Length(min=8), EqualTo('password_confirmation', message='Password should be match with confirm field.')],
        render_kw={
            'class': 'input input-bordered w-full focus:outline-2 focus:outline-blue-700',
            'placeholder': 'Password'
        }
    )
    password_confirmation = PasswordField(
        'password_confirmation',
        validators=[InputRequired(), DataRequired()],
        render_kw={
            'class': 'input input-bordered w-full focus:outline-2 focus:outline-blue-700',
            'placeholder': 'Confirm Password'
        }
    )