import streamlit as st
from main import svb, result

st.title("Laptop Price Model")
st.write(
    "Select your laptop specification so you would know your budget"
)

# Creation of selectioon  box and cooolecctionn  of user input
features = []
for keys in svb.keys():
    
    globals()[keys] = st.selectbox( keys ,
        [""] +  sorted(list(svb[keys])))
    features.append(globals()[keys])

# Sends user innput to  the result function in the main.py file 
price= result(features)

filled_box = [x for x in features if x != ""]
if st.button("Click"):
     # Output the user input
     if  len(filled_box) > 1:
         
        st.write(f"Your Budget should be £{round(price[0],-2):,}")
        st.write("Your specification are :- ")
        for fb in filled_box:
            st.write(f"{fb}")
  
     else:
        st.write("Enter at least two field")
        

