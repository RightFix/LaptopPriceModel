import streamlit as st
from main import svb, result

st.title("Laptop Price Model")
st.write(
    "Select your laptop specification so you would know your budget"
)

# Creation of selectioon  box and cooolecctionn  of user input
features = []
for keys in svb.keys():
    
    globals()[keys] = st.selectbox( keys.upper() ,
        [" "] +  sorted(list(svb[keys])) if keys != "inches" else [0] + sorted(list(svb[keys])))
    features.append(globals()[keys])

# Sends user innput to  the result function in the main.py file 
price= result(features)

filled_box = [x for x in features if x != "" or x != 0]
if st.button("Click"):
     if 0 not in features or len(filled_box) > 0:
         
        st.write(f"Your Budget should be £{round(price[0],-2):,}")
        st.write("Your specification are :- ")
        # output the user input
        for fb in filled_box:
            st.write(f"{fb}")
  
     else:
        st.write("Enter at least one field")
        

