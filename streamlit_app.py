import streamlit as st
import seaborn as sns
#import ipynb.fs.full.main 
from man import svb, result

st.title("Laptop Prediction Model App")
st.write(
    "Select your laptop specification So you would know your budget"
)

# Define the options for the selectbox
company_options = ["Apple", "HP", "Microsoft"]

# Create the selectbox
company_option = st.selectbox( 
  "Company:",
  company_options,
  index= None
)

for options in svb.keys():
  options = st.selectbox( 
    options ,
    sorted(list(svb[options])),
    index = None,
    placeholder = options,
    )
  
# Display the selected option

if st.button("Click"):
  st.write(f"Your Budget should be £...")
