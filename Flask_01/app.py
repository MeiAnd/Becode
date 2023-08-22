from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, InputRequired
from flask_bootstrap import Bootstrap
from markupsafe import Markup, escape
import mysql.connector
from config import Config #Import the Config class
import pymongo
# Integrating MongoDB
from pymongo import MongoClient
import bleach

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(Config) ## Use the Config class for configuration

#MongoDB conection
client = pymongo.MongoClient('mongodb://localhost:27017/')
db_mongo = client['contact']
collection= db_mongo['contact_flask']

# Create MySQL connection
db = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

# Create a cursor to execute MySQL queries
cursor = db.cursor()

# WTForms form class // Creation the fields HTML and
class MyForm(FlaskForm):
    name = StringField('First Name', validators=[DataRequired()])
    family_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Your e-mail', validators=[DataRequired(), Email()])
    subject = RadioField ('Subject',
                        choices=['Repair', 'Order', 'other'],
                        validators=[DataRequired()])
    gender = RadioField('Gender',
                        choices=['F', 'M'],
                        validators=[DataRequired()])
    message = TextAreaField('Message',
                        validators=[InputRequired()])

    submit = SubmitField('Submit')

# Sample route to fetch data from MySQL
@app.route('/data', methods=['GET'])
def get_data_from_mysql():
    cursor.execute("SELECT * FROM contact_messages")
    result = cursor.fetchall()
    return jsonify(result)

@app.route('/', methods=['GET', 'POST'])
def home():
    #Sanitize SQL
    form = MyForm()
    if form.validate_on_submit():
        name = escape(form.name.data)
        family_name = escape(form.family_name.data)
        subject = escape(form.subject.data)
        gender = escape(form.gender.data)
        message = escape(form.message.data)
        email = escape(form.email.data)
        country = escape(request.form['countries'])
        # Process the validated data, e.g., store it in the database.
        flash(f'Thank you {name} for your message, We will get back to you soon!', 'success')

        # Save the contact form data to the database - Prepared statements
        insert_query = "INSERT INTO contact_messages (name, family_name, subject, gender, message, email, country) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (name, family_name, subject, gender, message, email, country))
        db.commit()

        #Mongo integration
        data = {
        'name':escape(form.name.data),
        'family_name':escape(form.family_name.data),
        'subject':escape(form.subject.data),
        'gender':escape(form.gender.data),
        'message':escape(form.message.data),
        'email':escape(form.email.data),
        'country':escape(request.form['countries'])
        }

        collection.insert_one(data)

        return redirect(url_for('home'))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
