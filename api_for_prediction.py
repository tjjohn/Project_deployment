# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 16:41:04 2021

@author: tj john
"""
from flask import Flask, request,render_template
import numpy as np
import pickle
import pandas as pd

app=Flask(__name__)

pickle_in = open("lr.pkl","rb")
predict_Rem_Ind=pickle.load(pickle_in)


@app.route('/')                        # fn for homepage
def welcome():
    return render_template("index.html")

@app.route('/predict',methods=["Get"])  # fn for predicting
def predict_note_authentication():
    
  
    user_input_variable=request.args.get("user_label_text")
    
 #   prediction=predict_Rem_Ind.predict([[user_input]])
    print(user_input_variable)
    return "Hello The answer is"+str(user_input_variable)


if __name__=='__main__':
    app.run()
    