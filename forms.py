from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RoleField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    idUser  = StringField('Username: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Login')
    
class RegistrationForm(FlaskForm):
    idUser  = StringField('Username: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    role = RoleField('Role: ', validators=[DataRequired()])
    submit = SubmitField('Register')
    
class SearchForm(FlaskForm):
    keyword = StringField('Keyword: ', validators=[DataRequired()])
    submit = SubmitField('Search')