import os
from flask import Flask
from flask_sslify import SSLify
from flask import Flask, render_template, flash, request, send_from_directory
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


# App config.
DEBUG = True
app = Flask(__name__)
sslify = SSLify(app)

app.config.from_object(__name__)
app.config['SECRET_KEY'] = '101710171017'
app.config['OUTPUT_FOLDER'] = 'output'

class ReusableForm(Form):
    talk_topic = TextField('Topic: ', validators=[validators.required()])

@app.route('/output/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    outputs = os.path.join(app.root_path, app.config['OUTPUT_FOLDER'])
    return send_from_directory(directory=outputs, filename=filename)

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
    print('Errors: {}'.format(form.errors))

    if request.method == 'POST':
        talk_topic = request.form['talk_topic']
        print('Input talk topic: {}'.format(talk_topic))

        if form.validate():
            # Save the comment here.
            flash('Generating a talk on: ' + talk_topic)
        else:
            flash('All the form fields are required. ')

    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()