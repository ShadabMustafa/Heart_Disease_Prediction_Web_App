# Import libraries needed for the prediction function to work.
import pandas as pd
import numpy as np
import sklearn as sk
import matplotlib.pyplot as plot
import seaborn as sns
import pickle

# Load in the machine learning model.
loaded_RFCmodel = pickle.load(open("rfcHeartModel_v1.pkl", "rb"))


# Heart disease probability prediction function.
# Takes in a list and returns a string which is used to display results.
def predictHeartDisease(x:list):
    # List needs to be reshaped to be utilized for the prediction function.
    y = np.array(x)
    z = y.reshape(1,-1)
    prob = loaded_RFCmodel.predict_proba(z)
    striga,sliga ='',''
    if prob[0][0] > prob[0][1]:
        striga = ('% '+ str(round(((prob[0][0]) * 100.0),2)))
        sliga = "The probability of not having heart disease is " + striga
    else:
        striga = ('% ' + str(round(((prob[0][1]) * 100.0), 2)))
        sliga = "The probability of having heart disease is " + striga
    return  sliga


