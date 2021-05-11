from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")

class RegisterForm(Form):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    name = StringField("name", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])


class PostForm(Form):
    cpf = StringField("cpf", validators=[DataRequired()])
    cliente = StringField("cliente", validators=[DataRequired()])
    telefone = StringField("telefone", validators=[DataRequired()])
    email_cli = StringField("email_cli", validators=[DataRequired()])

class Registro(Form):

    cpf = StringField("cpf")
    cliente = StringField("cliente")
    telefone = StringField("telefone")
    email_cli = StringField("email_cli")
