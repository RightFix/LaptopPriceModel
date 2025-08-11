import streamlit as st
#import ipynb.fs.full.main 

st.title("Laptop Prediction Model App")
st.write(
    "Select your laptop specification So you would know your budget"
)

# Define the options for the selectbox
options = ["Option A", "Option B", "Option C"]

# Create the selectbox
selected_option = st.selectbox(
    "Company:",  # Label for the selectbox
    options             # List of options
)

# Display the selected option
st.write("You selected:", selected_option)

if st.button("Click"):
  st.write(f"Your Budget should be .... {result()}")
