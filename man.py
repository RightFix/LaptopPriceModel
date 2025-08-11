#!/usr/bin/env python
# coding: utf-8

# Contributors
# 
# Ude Righteousness Nwannennaya - 23/EG/CO/014,
# 
# Essien Ubong Bassey - 23/EG/CO/009,

# Import Necessary Libraries In This Cell Below

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
#get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


df = pd.read_csv("dataset/laptop_price.csv")


# Dataset Overview

# In[ ]:


df.head()


# In[ ]:


df.tail()


# In[ ]:


df.columns


# In[ ]:


df.sample(5)


# In[ ]:


df.info()


# In[ ]:


df.describe()


# In[ ]:


df.describe(include = "object")


# Data Cleaning And Analysis

# In[ ]:


#Standardise columns name by making it lowercase
df.columns = df.columns.str.replace(" ","_").str.lower()
df.columns


# In[ ]:


# Dropping the laptop_ID column because it isn't need in the analysis
# Using data variable instead of df so as not to tamper with the original dataset
data = df.drop(columns= "laptop_id")
data.head()


# In[ ]:


# Remove duplicate samples
data = data.drop_duplicates()
data.head()


# In[ ]:


data.isnull().sum()


# In[ ]:


# Filling null value with the mode of their column
data.gpu = data.gpu.fillna(data.gpu.mode()[0])
data.weight= data.weight.fillna(data.weight.mode()[0])
data.isnull().sum()


# In[ ]:


#value count of each columns
#for col in data.columns:
#  print(data[col].value_counts())
#  print("\n\n")


# In[ ]:


# Countplot for all non-numeric columns

#for cols in data.select_dtypes(include= "object"):
 #plt.figure(figsize = (20,5))
 #sns.countplot(data= data, x =cols)
 #plt.title(f"Count Plot For {cols}".capitalize())
# plt.xticks(rotation = 90)
 #plt.show()


# In[ ]:


# Barplot for all non-numeric columns by Price

#for cols in data.select_dtypes(include= "object"):
 #plt.figure(figsize = (20,5))
# sns.barplot(data= data, x =cols, y= "price_euros")
 #plt.title(f"Bar Plot For {cols} Vs Price in Euros(£)".capitalize())
 #plt.xticks(rotation = 90)
# plt.show()


# In[ ]:


plt.close()


# In[ ]:


data.info()


# creation And Training Models

# In[ ]:


x = data.drop(["price_euros"], axis=1 ) # Independent variable (predictor)
y = data["price_euros"] # Dependent variable (target)


# In[ ]:


x_train, x_test, y_train, y_test = split(x, y, test_size= 0.1, random_state=42)


# In[ ]:


print(x_train.shape, y_train.shape)


# In[ ]:


# Identify categorical & numeric columns
cat_cols = x.select_dtypes(include=['object']).columns
num_cols = x.select_dtypes(exclude=['object']).columns


# In[ ]:


#Transformer: Encode categorical + scale numeric
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols),
        ('num', StandardScaler(), num_cols)
    ]
)


# In[ ]:


# Pipeline: preprocessing + model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])


# In[ ]:


# Train
model.fit(x_train, y_train)


# In[ ]:


# Predict
predictions = model.predict(x_test)

#print("Predictions:", predictions)


# In[ ]:


# Evaluate
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

#print("Mean Squared Error:", mse)
#print("R² Score:", r2)


# Testing Model With External Values

# In[ ]:


# user input would be taken care of in this cell
#a, b, c, d, e,f ,g, h,i,j = "Apple", "MacBook Pro", "", "1.4", "", "", "", "", "", "3.2kg"
def result(a, b, c, d ,e, f, g, h, i, j):
   # creating an empty dictionary whenever it is called
   test_data = {}
   for test_cols in x.columns:
          test_data.update({test_cols:[""]})

   test_data["company"]= a
   test_data["product"] = b
   test_data["typename"] = c
   test_data["inches"] = float(d)
   test_data["screenresolution"] = e
   test_data["cpu"] = f
   test_data["memory"] = g
   test_data["gpu"]= h
   test_data["opsys"] = i
   test_data["weight"] = j

   test_data_df = pd.DataFrame(test_data)
   #print(test_data_df)

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

#print(result(a, b, c, d, e, f, g, h, i, j))



# Streamlit variables for the Selection Box Variable (SVB)

# In[ ]:


svb = {}
for cols in x.columns:
    svb[cols] = set(x[cols].tolist())


# In[ ]:




