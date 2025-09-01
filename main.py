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

# Defining dataset to a variable
df = pd.read_csv("dataset/laptop_price.csv")


# Dropping the laptop_ID column because it isn't need in the analysis
# Using data variable instead of df so as not to tamper with the original dataset
data = df.drop(columns= "laptop_ID")

# Standardise columns name by making it understandable
data = data.rename(columns = {"TypeName":"Type", "Cpu" :"CPU", "Gpu": "GPU", "Ram" : "RAM", "Price_euros": "Price(£)", "OpSys": "Operating_System", "ScreenResolution": "Screen_Resolution"})

# Remove duplicate samples
data = data.drop_duplicates()

# Filling null value with the mode of their column
data.GPU = data.GPU.fillna(data.GPU.mode()[0])
data.Weight= data.Weight.fillna(data.Weight.mode()[0])

# Creation And Training Models

x = data.drop(columns =["Price(£)", "Inches"], axis=1 ) 
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

   test_data = {test_cols :[feature[idx]] for test_cols, idx in zip(x.columns, range(len(x.columns)))}
   
   test_data_df = pd.DataFrame(test_data)
  
   # test data to numeric because of category columns

   onehot_encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

   for cols in test_data_df.select_dtypes(include ="object").columns:
      # Fit and transform the column
      encoded_features = onehot_encoder.fit_transform(test_data_df[[cols]])
      # Create a DataFrame from the encoded features with appropriate column names
      encoded_df = pd.DataFrame(encoded_features, columns=onehot_encoder.get_feature_names_out([cols]))
      #Concatenate with the original DataFrame
      df_encoded = pd.concat([test_data_df, encoded_df], axis=1)

   return model.predict(df_encoded)

# Streamlit variables for the Selection Box Variable (SVB)

svb = {}
for cols in x.columns:
    svb[cols] = set(x[cols].tolist())
