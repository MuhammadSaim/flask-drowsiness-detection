from app.models.user import User
from wtforms.validators import ValidationError


class EmailExists:

    def __init__(self, model=User, exclude=None, message=None):
        self.model = model
        self.exclude = exclude
        if not message:
            message = "Email is already in use."
        self.message = message

    def __call__(self, form, field):
        user = self.model.query.filter_by(email=field.data)
        if not self.exclude:
            user.filter_by(id=self.exclude)
        if user.first():
            raise ValidationError(self.message)