from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    BooleanField,
    SelectField,
    SubmitField,
    MultipleFileField,
)
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, Email, Regexp, URL
from wtforms import ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import Role, User, Scene


# forms section
class ThreadForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(0, 256)])
    body = TextAreaField("Body", render_kw={"class": "form-control", "rows": 5})
    scene = SelectField(
        u"Post to Scene (Optional)",
        choices=[
            ("", ""),
            ("Los Angeles", "Los Angeles"),
            ("NYC", "NYC"),
            ("Chicago", "Chicago"),
        ],
    )
    type = "thread"
    image = FileField("Post Thumbnail (Optional)")
    submit = SubmitField("Submit")


# forms section
class LinkForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(0, 256)])
    body = TextAreaField(
        "Body (Optional)", render_kw={"class": "form-control", "rows": 5}
    )
    link = StringField("Link (Optional) (e.g. Youtube links) ")
    image = FileField("Upload an Image (Optional)")
    scene = QuerySelectField(
        "Post to a Scene (Optional)",
        query_factory=lambda: Scene.query.all(),
        get_pk=lambda a: a.id,
        get_label=lambda a: a.name,
    )
    type = "link"

    submit = SubmitField("Submit")


class EditProfileAdminForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(1, 64),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_.]*$",
                0,
                "Usernames must have only letters, numbers, dots or " "underscores",
            ),
        ],
    )
    confirmed = BooleanField("Confirmed")
    role = SelectField("Role", coerce=int)
    name = StringField("Real name", validators=[Length(0, 64)])
    location = StringField("Location", validators=[Length(0, 64)])
    about_me = TextAreaField("About me")
    image = FileField("Change Profile Picture")
    submit = SubmitField("Submit")

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [
            (role.id, role.name) for role in Role.query.order_by(Role.name).all()
        ]
        self.user = user

    def validate_email(self, field):
        if (
            field.data != self.user.email
            and User.query.filter_by(email=field.data).first()
        ):
            raise ValidationError("Email already registered.")

    def validate_username(self, field):
        if (
            field.data != self.user.username
            and User.query.filter_by(username=field.data).first()
        ):
            raise ValidationError("Username already in use.")


class EditProfileForm(FlaskForm):
    name = StringField("Real name", validators=[Length(0, 64)])
    location = StringField("Location", validators=[Length(0, 64)])
    about_me = TextAreaField("About me")
    image = FileField("Change Profile Picture")
    submit = SubmitField("Submit")


class CommentForm(FlaskForm):
    body = TextAreaField("", render_kw={"class": "form-control", "rows": 3})
    submit_comment = SubmitField("Submit")


class SearchForm(FlaskForm):
    text = StringField("")
    submit_search = SubmitField("Submit")


class SceneForm(FlaskForm):
    name = StringField("Name", validators=[Length(0, 64)])
    description = TextAreaField(
        "Description", render_kw={"class": "form-control", "rows": 2}
    )
    category = SelectField("Category", choices=[("Topic", "Topic"), ("City", "City")])
    submit = SubmitField("Submit")
