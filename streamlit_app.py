import streamlit as st
from main import svb, result

st.title("Laptop Price Model")
st.write(
    "Select your laptop specification so you would know your budget"
)

features = []
weight= svb.["weight"]
we= svb.pop("weight")
for keys in svb.keys():
  globals()[keys] = st.selectbox( keys.upper() , [" "] + sorted(list(svb[keys])))
  features.append(globals()[keys])

weight  = st.selectbox( "weight".upper() , [0] + sorted(list(we)))
features = features.append(weight)
price= result(features)

if st.button("Click"):
  st.write(f"Your Budget should be £{round(price[0],-2):,}")
  st.write("Your specification are :- ")
  features_name = [x for x in svb.keys()]
  for f, fn in zip(features, features_name):
        st.write(f" {fn}: {f}")

