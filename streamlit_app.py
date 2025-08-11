import streamlit as st
#import ipynb.fs.full.main 

st.title("Laptop Prediction Model App")
st.write(
    "Select your laptop specification So You would know "
)

# Define the options for the selectbox
options = ["Option A", "Option B", "Option C"]

# Create the selectbox
selected_option = st.selectbox(
    "Choose an option:",  # Label for the selectbox
    options             # List of options
)

# Display the selected option
st.write("You selected:", selected_option)

if st.button("Click"):
  st.write("Your Budget should be ....")
