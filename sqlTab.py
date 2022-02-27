# This file is used for data queries needed for plotly dash app to work as intended.
# Libraries needed to connect flask app to database.
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, select, MetaData, Table, and_


# Second Flask app created to connect to database.
app = Flask(__name__)
app.secret_key = 'secretKey'

app.config.update(
# Connects flask app to heroku postgres database.
SQLALCHEMY_DATABASE_URI = "postgres://tehvifpwvlxicz:ae34119144f7bcfc5fa105cd4f9ff4654c21087d0f59d9ad4039261b4f5a7630@ec2-34-194-171-47.compute-1.amazonaws.com:5432/da80e0bd7c30rl",
SQLALCHEMY_TRACK_MODIFICATIONS = False
)

# Database model connected to flask app database.
db = SQLAlchemy(app)

# Class to access columns of dataset.
class Hd_data(db.Model):
    __tablename__ = 'hdTable2'
    id = db.Column(db.Integer,primary_key=True)
    age = db.Column(db.Float)
    sex = db.Column(db.Float)
    cp = db.Column(db.Float)
    trestbps = db.Column(db.Float)
    chol = db.Column(db.Float)
    fbs = db.Column(db.Float)
    restecg = db.Column(db.Float)
    thalach = db.Column(db.Float)
    exang = db.Column(db.Float)
    oldpeak = db.Column(db.Float)
    slope = db.Column(db.Float)
    ca = db.Column(db.Float)
    thal = db.Column(db.Float)
    target = db.Column(db.Float)


    def __init__(self,age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
                 ,target):
        self.age = age
        self.sex = sex
        self.cp = cp
        self.trestbps = trestbps
        self.chol = chol
        self.fbs = fbs
        self.restecg = restecg
        self.thalach = thalach
        self.exang = exang
        self.oldpeak = oldpeak
        self.slope = slope
        self.ca = ca
        self.thal = thal
        self.target = target

    def __repr__(self):
        return f"{self.age}"

    def __float__(self):
        return self.age

    # Returns entire record of data in list format.
    def list(self):
        return [self.age,self.sex,self.cp
                ,self.trestbps,self.chol,self.fbs,self.restecg,self.thalach,self.exang
                ,self.oldpeak,self.slope,self.ca,self.thal,self.target]

# Get count of how many records have heart disease marked as present, needed for plotly pie graph.
def hdPresent():
    dataz2 = (Hd_data.query.filter_by(target = '1').all())
    y = len(dataz2)
    return y

# Get count of how many records have heart disease marked as non-present, needed for plotly pie graph.
def hdNotPresent():
    dataz3 = (Hd_data.query.filter_by(target='0').all())
    y = len(dataz3)
    return y

# Get age column of values, needed for plotly histogram graph.
def ageVals():
    dataz = ((Hd_data.query.order_by(Hd_data.age).all()))
    liz = []
    i=0
    while i < 303:
        x = dataz[i]
        y = x.list()
        liz.append((y)[0])
        i += 1
    return liz

# Get chest pain column + target/heart disease presence column of values, needed for plotly bar graph.
def cpHDpresent():
    dataz = ((Hd_data.query.all()))
    liz = []
    i=0
    while i < 303:
        x = dataz[i]
        y = x.list()
        liz.append([y[2],y[13]])
        i += 1
    return liz

# Function adds in string values instead of numerical values, needed for plotly bar graph.
def cpHDpresent2():
    dataz = ((Hd_data.query.all()))
    liz = []
    i=0
    while i < 303:
        x = dataz[i]
        y = x.list()

        if y[2] == 0:
            if y[13] == 0:
                liz.append((['Typical Angina','Not Present']))
            else:
                liz.append((['Typical Angina','Present']))

        elif y[2] == 1:
            if y[13] == 0:
                liz.append((['Atypical Angina','Not Present']))
            else:
                liz.append((['Atypical Angina','Present']))

        elif y[2] == 2:
            if y[13] == 0:
                liz.append((['Non-anginal pain','Not Present']))
            else:
                liz.append((['Non-anginal pain','Present']))

        elif y[2] == 3:
            if y[13] == 0:
                liz.append((['Asymptomatic', 'Not Present']))
            else:
                liz.append((['Asymptomatic', 'Present']))

        i += 1
    return liz














