# Heart_Disease_Prediction_Web_App

## Description
A web application used to predict the probability of an individual having heart disease.
Scikit-learn library to create a random forest classifier machine learning algorithm that is 83.60% accurate.
Stylized web application via Bootstrap 4.
Incorporated data visualization with Dash Plotly.
PostgreSQL database used for visualization interactiviness.
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
![image](https://user-images.githubusercontent.com/69401254/166811678-5f33a69a-56bf-49d9-997a-fc91f0278acf.png)
![image](https://user-images.githubusercontent.com/69401254/166811712-440568f2-b684-4086-a849-c1dacf87d5d5.png)


## Application Files Break down
 
* static:
  Holds favicon and image of correlation matrix

* templates:
holds html files

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

* PDF Heart Disease Model v1 - Jupyter:
PDF of jupyter notebook used to
develop the machine learning model
for easier reading and no setup

* Heart Disease Model v1.ipynb:
jupyter notebook used to develop
the machine learning model
