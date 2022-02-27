# Shadab Mustafa
# Student ID: 001236391
# Application is hosted already on heroku at https://heart-disease-prediction-site.herokuapp.com/ for easy access.
# Imported libraries for prediction tab and entire program to work.
from flask import Flask, render_template, request
from predictionFunction import predictHeartDisease
from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
flash
)

# User class to hold user login info.
class User:
    def __init__(self, id:int, username:str, password:str):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

# Only one user needed for now.
# List to hold users
users = []
users.append(User(id=1, username='admin', password='admin'))

# Basic app creation
app = Flask(__name__)
# secret key needed for login purposes
app.secret_key = 'secretKey'

# Confirms user is signed in.
@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

# Login form connects to server.
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']

        # Clears login in form if user types in wrong password or user name.
        try:
            user = [x for x in users if x.username == username][0]
            if user and user.password == password:
                session['user_id'] = user.id
                return redirect(url_for('prediction'))
        except Exception:
            return redirect(url_for('login'))
    return render_template('login.html')

# Link dash app to flask app
from dashApp import createDashApp
createDashApp(app)

# Prediction tab of site rendered after login.
@app.route('/prediction')
def prediction():
    # Confirms user is signed in.
    if not g.user:
        return redirect(url_for('login'))
    return render_template('predictionTab.html')

# Prediction result page linked to python code so prediction
# algorithm can get inputs needed for the result.
@app.route('/result')
def result():
    # Confirms user is signed in.
    if not g.user:
        return redirect(url_for('login'))
    try:
        inputLs = []
        age = float(request.args.get('age'))
        sex = float(request.args.get('sex'))
        cp = float(request.args.get('cp'))
        trestbps = float(request.args.get('trestbps'))
        chol = float(request.args.get('chol'))
        fbs = float(request.args.get('fbs'))
        restecg = float(request.args.get('restecg'))
        thalach = float(request.args.get('thalach'))
        exang = float(request.args.get('exang'))
        oldpeak = float(request.args.get('oldpeak'))
        slope = float(request.args.get('slope'))
        ca = float(request.args.get('ca'))
        thal = float(request.args.get('thal'))
        inputLs.extend([age,sex,cp,trestbps,chol,fbs,restecg,thalach
                       ,exang,oldpeak,slope,ca,thal])
        endResult = predictHeartDisease(inputLs) +'.'
        return render_template('resultz.html', endResult=endResult)
    except Exception:
            return redirect(url_for('prediction'))

# Application is run.
if __name__ == '__main__':
    app.run(debug=False)