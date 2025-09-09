""" 
    This file contains the necessary lines of code needed to run the model and needed for the steamlit web application. It is almost if not at all the same with the main.ipynb file

 Contributors: 
 Okon Imoh Daniel
 Wilson Isreal John
 Ude Righteousness Nwannennaya 
 Libang Success Obi
 Ebong Nsikanabasi Samuel 
 Bassey Shine Joseph
 Uyeh Samuel John
 Essien Ubong Bassey
 Micheal Kubiatabasi Edet
 Peter Justice Emmanuel
"""
# Import Necessary Libraries 

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import streamlit as st
from streamlit_autorefresh import st_autorefresh

# Defining dataset to a variable
df = pd.read_csv("dataset/laptop_price.csv")


# Dropping the laptop_ID column because it isn't need in the analysis
# Using data variable instead of df so as not to tamper with the original dataset
data = df.drop(columns= "laptop_ID")

# Standardise columns name by making it understandable
data = data.rename(columns = {"TypeName":"Type", "Cpu" :"CPU", "Gpu": "GPU", "Ram" : "RAM", "Price_euros": "Price(£)", "OpSys": "Operating System", "ScreenResolution": "Screen Resolution"})

# Remove duplicate samples
data = data.drop_duplicates()

# Model Creation And Training
x = data.drop(columns = ["Price(£)", "Inches", "Weight", "GPU", "Product"], axis=1 ) # Droping some columns because it is not needed
y = data["Price(£)"] # Dependent variable (target)

x_train, x_test, y_train, y_test = split(x, y, test_size= 0.25, random_state=25)

# Identify categorical & numeric columns
cat_cols = x.select_dtypes(include=['object']).columns
num_cols = x.select_dtypes(exclude=['object']).columns

#Transformer: Encode categorical + scale numeric
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols),
        ('num', StandardScaler(), num_cols)
    ]
)

# Pipeline: preprocessing + model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Train
model.fit(x_train, y_train)

def result(feature):

   test_data = {test_cols :[feature[idx]] for test_cols, idx in enumerate(x.columns)}
   
   test_data_df = pd.DataFrame(test_data)
   predicted_price = model.predict(test_data_df)

   return predicted_price


# Streamlit variables for the Selection Box Variable (SVB)
svb = {}
for cols in x.columns:
    svb[cols] = set(x[cols].tolist())

st.title("Laptop Price Model")
st.write(
    "Select your laptop specification so you would know your budget"
)
# Prevent all from sleeping
st_autorefresh(interval = 60000, key= "refresh")
# Creation of selectioon  box and collection  of user input

features = []
for keys in svb.keys():
    
    globals()[keys] = st.selectbox( keys ,[""] +  sorted(list(svb[keys])))
    features.append(globals()[keys])

# Sends user input to  the result function in when te button is clicked
price= result(features)

filled_box = [x for x in features if x != ""]
if st.button("Click"):
     # Output the user input
     if  len(filled_box) > 0:
         
        st.write(f"Your Budget should be £{round(price[0],-2):,}")
        st.write("Your specification are :- ")
        for fb in filled_box:
            st.write(f"{fb}")
  
     else:
        st.write("Enter at least one field") 