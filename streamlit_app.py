import streamlit as st
#import ipynb.fs.full.main 

st.title("Laptop Prediction Model App")
st.write(
    "Select your laptop specification So you would know your budget"
)

# Define the options for the selectbox
company_options = ["","Apple", "HP", "Microsoft"]

# Create the selectbox
company_option = st.selectbox(
    "Company:",  # Label for the selectbox
    company_options             # List of options
)

# Display the selected option
a = company_option
if st.button("Click"):
  st.write(f"Your Budget should be £...")
