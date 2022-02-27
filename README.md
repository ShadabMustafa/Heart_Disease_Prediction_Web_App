# Heart_Disease_Prediction_Web_App

## Description
A web application used to predict the probability of an individual having heart disease.
Scikit-learn library to create a random forest classifier machine learning algorithm that is 83.60% accurate.
Stylized web application via Bootstrap 4.
Incorporated data visualization with Dash Plotly.
Flask used to link pages together.
Deployed on to Heroku cloud.

## Application Deployed Here
https://heart-disease-prediction-site.herokuapp.com/
Login in with "admin" as both username and password.

![image](https://user-images.githubusercontent.com/69401254/155863759-6192daaf-e152-4450-8b2f-bcb574992880.png)

Navigation bar and prediction page will load in:

![image](https://user-images.githubusercontent.com/69401254/155863777-abc56bd3-0acb-42d2-8bf1-e4f43891ffeb.png)

Find data visualizations here:

![image](https://user-images.githubusercontent.com/69401254/155863789-122df56f-a21f-4bff-9883-905f197dd1e8.png)

## Application Files Break down
* Heart site v1 pkg:
  Application root directory folder
 
* static:
  Holds favicon and image of correlation matrix

* templates:
holds html files

* venv:
virtual environment(holds libraries)

* dashApp.py:
Dash app, has data visualizations

* heart-diseaseV3.csv:
raw dataset, inside a dashApp table

* main.py:
main file to run program, interacts with predictiontab.html and resultz.html

* predictionFunction.py:
holds the heart disease probability prediction function

* Procfile:
File used to setup gunicorn library. That is needed for Heroku deployment

* requirements.txt:
has list of libraries used during the project, needed for Heroku deployment

* rfcHeartModel_v1.pkl:
machine learning model, developed in a Jupyter notebook.

* runtime.txt:
specifies the python version 3.6.15 for the Heroku server to run the program on

* sqlTab.py:
holds a second flask app used to interact with the PostgreSQL db

* Documentation and Machine learning model code:
folder holds documentation and the jupyter notebook used to develop the machine learning model

* PDF Heart Disease Model v1 - Jupyter:
PDF of jupyter notebook used to
develop the machine learning model
for easier reading and no setup

* Heart Disease Model v1.ipynb:
jupyter notebook used to develop
the machine learning model
