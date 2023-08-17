import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotly import graph_objs as go
import pickle

loaded_model = pickle.load(open('wine_quality_predition.pkl', 'rb'))
sc = pickle.load(open('sc.pkl', 'rb'))

data=pd.read_csv("winequality.csv")

data['best quality'] = [1 if x > 5 else 0 for x in data.quality]

st.header("WINE QUALITY PREDICTION")

nav=st.sidebar.radio("navigation",["PREDICT","VISUALIZATION","CONTRIBUTE"])
if nav=="VISUALIZATION":
    st.header("HOME")
    st.write("VIEWING AND VISUALIZING THE DATASET")
    st.success("Tick below to view the dataset")
    if st.checkbox("view dataset"):
        st.dataframe(data,width=500,height=500)
    
    graph = st.selectbox("What kind of Graph ? ",["Non-Interactive","Interactive"])
    val = st.slider("Filter data using amount of alcohol",7,15)
    data = data.loc[data["alcohol"]>= val]
    if graph=="Non-Interactive":
        x=plt.figure(figsize = (10,5))
        plt.scatter(data["alcohol"],data["quality"])
        plt.ylim(0)
        plt.xlabel("amount of alcohol")
        plt.ylabel("quality of wine")
        plt.tight_layout()
        st.pyplot(x)
    if graph == "Interactive":
        layout =go.Layout(
            xaxis = dict(range=[7,15]),
            yaxis = dict(range =[0,10])
        )
        fig = go.Figure(data=go.Scatter(x=data["alcohol"], y=data["quality"], mode='markers'),layout = layout)
        st.plotly_chart(fig)
    st.write("A PROJECT BY")
    st.markdown("<h1 style='font-size: 20px;'>SYAM KRISHNA REDDY PULAGAM</h1>", unsafe_allow_html=True)
if nav=="PREDICT":
    st.image("wine_quality_prediction.jpg",width=500)
    st.header("prediction")
    st.title("Know your Wine Quality")
    type1=st.selectbox("Type",['white','red'],index=0)
    if type1=="white":
        type1=1
    else:
        type1=0
    fixed_acidity=st.number_input("fixed acidity",min_value=3.800000,max_value=15.900000,value=3.900000,step=0.1)
    volatile_acidity=st.number_input("volatile acidity",min_value=0.0,max_value=1.580000,value=1.0,step=0.1)
    citric_acid=st.number_input("citric_acid",min_value=0.0,max_value=1.660000,value=1.0,step=0.1)
    residual_sugar=st.number_input("residual_sugar",min_value=0.0,max_value=65.800000,value=1.0,step=0.1)
    chlorides=st.number_input("chlorides",min_value=0.0,max_value=0.611000,value=0.1,step=0.1)
    free_sulfur_dioxide=st.number_input("free_sulfur_dioxide",min_value=0.0,max_value=289.000000,value=1.0,step=0.1)
    total_sulfur_dioxide=st.number_input("total_sulfur_dioxide",min_value=0.0,max_value=440.000000	,value=1.0,step=0.1)
    density=st.number_input("density",min_value=0.0,max_value=1.038980,value=1.0,step=0.1)
    pH=st.number_input("pH",min_value=0.0,max_value=4.010000,value=1.0,step=0.1)
    sulphates=st.number_input("sulphates",min_value=0.0,max_value=2.0,value=1.0,step=0.1)
    alcohol=st.number_input("alcohol",min_value=0.0,max_value=14.900000,value=1.0,step=0.1)
    if st.button("PREDICT"):
        classifier=loaded_model.predict(sc.transform([[type1, fixed_acidity, volatile_acidity, citric_acid,residual_sugar, chlorides, free_sulfur_dioxide,total_sulfur_dioxide, density, pH, sulphates, alcohol]]))
        if classifier == 0:
            st.error("NOT GOOD")
            st.write("<span style='font-size: 30px;'>QUALITY OF WINE IS NOT GOOD</span>", unsafe_allow_html=True)
        else:
            st.success("GOOD")
            st.write("<span style='font-size: 30px;'>QUALITY OF WINE IS GOOD</span>", unsafe_allow_html=True)
    st.write("")	
    st.write("A PROJECT BY")
    st.markdown("<h1 style='font-size: 20px;'>SYAM KRISHNA REDDY PULAGAM</h1>", unsafe_allow_html=True)
if nav=="CONTRIBUTE":
    st.header("Contribute to our data")
    type=st.selectbox("Type",['white','red'],index=0)
    fixed_acidity=st.number_input("fixed acidity",min_value=3.800000,max_value=15.900000,value=3.900000,step=0.1)
    volatile_acidity=st.number_input("volatile acidity",min_value=0.0,max_value=1.580000,value=1.0,step=0.1)
    citric_acid=st.number_input("citric_acid",min_value=0.0,max_value=1.660000,value=1.0,step=0.1)
    residual_sugar=st.number_input("residual_sugar",min_value=0.0,max_value=65.800000,value=1.0,step=0.1)
    chlorides=st.number_input("chlorides",min_value=0.0,max_value=0.611000,value=0.1,step=0.1)
    free_sulfur_dioxide=st.number_input("free_sulfur_dioxide",min_value=0.0,max_value=289.000000,value=1.0,step=0.1)
    total_sulfur_dioxide=st.number_input("total_sulfur_dioxide",min_value=0.0,max_value=440.000000	,value=1.0,step=0.1)
    density=st.number_input("density",min_value=0.0,max_value=1.038980,value=1.0,step=0.1)
    pH=st.number_input("pH",min_value=0.0,max_value=4.010000,value=1.0,step=0.1)
    sulphates=st.number_input("sulphates",min_value=0.0,max_value=2.0,value=1.0,step=0.1)
    alcohol=st.number_input("alcohol",min_value=0.0,max_value=14.900000,value=1.0,step=0.1)
    quality=st.number_input("quality",min_value=0,max_value=10,step=1)
    if st.button("submit"):
        st.success("Submitted")
    st.write("A PROJECT BY")
    st.markdown("<h1 style='font-size: 20px;'>SYAM KRISHNA REDDY PULAGAM</h1>", unsafe_allow_html=True)