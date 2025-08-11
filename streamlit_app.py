import streamlit as st
#import ipynb.fs.full.main 
from man import svb, result

st.title("Laptop Prediction Model App")
st.write(
    "Select your laptop specification So you would know your budget"
)

for options in svb.keys():
  options = st.selectbox( 
    options.capitalize() ,
    sorted(list(svb[options])),
    index = None,
    placeholder = options,
    )
  
# Display the selected option

if st.button("Click"):
  st.write(f"Your Budget should be £...")
