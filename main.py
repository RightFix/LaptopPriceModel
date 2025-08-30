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

#Standardise columns name by making it lowercase
df.columns = df.columns.str.replace(" ","_").str.lower()

# Dropping the laptop_ID column because it isn't need in the analysis
# Using data variable instead of df so as not to tamper with the original dataset
data = df.drop(columns= "laptop_id")

# Remove duplicate samples
data = data.drop_duplicates()

# Filling null value with the mode of their column
data.gpu = data.gpu.fillna(data.gpu.mode()[0])
data.weight= data.weight.fillna(data.weight.mode()[0])


# creation And Training Models

x = data.drop(columns =["price_euros"], axis=1 ) # Independent variable (predictor)
y = data["price_euros"] # Dependent variable (target)

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


# Predict
predictions = model.predict(x_test)


def result(feature):
   # creating an empty dictionary whenever it is called
   test_data = {}
   for test_cols in x.columns:
          test_data.update({test_cols:[""]})

   test_data["company"]= feature[0]
   test_data["product"] = feature [1]
   test_data["typename"] = feature[2]
   test_data["inches"] = feature[3]
   test_data["screenresolution"] = feature[4]
   test_data["cpu"] = feature[5]
   test_data["memory"] = feature[6]
   test_data["gpu"]= feature[7]
   test_data["opsys"] = feature[8]
   test_data["weight"] = feature[9]

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
