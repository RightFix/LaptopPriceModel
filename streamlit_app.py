import re
import streamlit as st
from main import svb, result

st.title("Laptop Price Model")
st.write(
    "Select your laptop specification so you would know your budget"
)

pattern = r"[A-Z][a-z][0-9]"
features = []
for keys in svb.keys():
    if re.findall(pattern, list(svb.values()[0])):
        globals()[keys] = st.selectbox( keys.upper() , [" "] +  sorted(list(svb[keys])))
        features.append(globals()[keys])
    else:
        globals()[keys] = st.selectbox( keys.upper() , [0] + sorted(list(svb[keys])))
        features.append(globals()[keys])

price= result(features)

if st.button("Click"):
  if " " in features or 0 in features:
    st.write("Incomplete input")
  
  else:
    st.write(f"Your Budget should be £{round(price[0],-2):,}")
    st.write("Your specification are :- ")
    features_name = [x for x in svb.keys()]
    for f, fn in zip(features, features_name):
        st.write(f" {fn}: {f}")

