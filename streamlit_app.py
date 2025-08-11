import streamlit as st
#from ipynb.fs.full.main import result, svb
from man import svb, result

st.title("Laptop Prediction Model App")
st.write(
    "Select your laptop specification So you would know your budget"
)

features = [company, product, typename, screeenresoluttion, cpu, ram, memory, gpu, opsys, weight ]  
for options in features:
  options = st.selectbox( 
    options.capitalize() ,
    sorted(list(svb[str(options)])),
    index = None,
    placeholder = options,
    )

price= result(features)
if st.button("Click"):
  st.write(f"Your Budget should be £{price[0]}")
  st.write(f"Your Budget should be £{features}")

