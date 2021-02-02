# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 17:33:11 2021

@author: panka
"""

import numpy as np
import pandas as pd
import streamlit as st
import pickle

pickel_in = open("C:/Users/panka/Documents/Project 2020/classifier.pkl","rb")
rm=pickle.load(pickel_in)

def predictions(pH,EC,OC,N,P,K,S,Zn,Fe,Cu,Mn,B):
    pred=rm.predict([[pH,EC,OC,N,P,K,S,Zn,Fe,Cu,Mn,B]])
    print(pred)
    return(pred[0])

def main():
    st.title("Crop Prediction From Soil Analysis")
    
    st.write(""" ##### All the fields are compulsory(*)""")

    f,l=st.beta_columns(2)
    pH = f.text_input("pH(0 to 14)*")
    EC = l.text_input("Electrical Conductivity EC (0.2 to 10 dSm/m)*")
    f,l=st.beta_columns(2)
    OC = f.text_input("Organic Carbon OC (0.2 to 2 %)*")
    N = l.text_input("Nitrogen N(100 to 700 Kg/Ha)*")
    f,l=st.beta_columns(2)
    P = f.text_input("Phosphorus P (10 to 80 Kg/Ha)*")
    K = l.text_input("Potassium K(150 to 800 Kg/Ha)*")
    f,l=st.beta_columns(2)
    S = f.text_input("Sulfur S(2 to 50 PPM)*")
    Zn = l.text_input("Zinc Zn(0.2 to 5 PPM)*")
    f,l=st.beta_columns(2)
    Fe = f.text_input("Iron Fe(2 to 20 PPM)*")
    Cu = l.text_input("Copper Cu(0.2 to 5 PPM)*")
    f,l=st.beta_columns(2)
    Mn = f.text_input("Manganese Mn(2 to 25 PPM)*")
    B = l.text_input("Boron B(0.2 to 5 PPM)*")
    
    
    result=""
    if st.button("Predict"):
        result=predictions(pH,EC,OC,N,P,K,S,Zn,Fe,Cu,Mn,B)
    st.success('Crop Predicated is : {}'.format(result))
    
    st.write("""
             #### Note:Enter Data Related to Only following Districts And Talukas of Maharashtra:     
       """)
    st.write("""##### Shirala,Jamner,Dhule,Malegaon,Nashik,Junnar,Mulshi,Yavatmal,Washim,Wani,Nanded,Karvir
                """)
    st.write("""
             ##### Mukhed,Buldana,Khamgaon,Patan,Koregaon,Karad,Kagal,Nagpur(Rural),Bhusawal,Jalgaon,Akola.
             """) 
if __name__=='__main__':
    main()
    
    
