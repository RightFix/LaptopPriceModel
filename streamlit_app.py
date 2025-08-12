import streamlit as st
#from ipynb.fs.full.main import result, svb
from main import svb, result

st.title("Laptop Price Model")
st.write(
    "Select your laptop specification so you would know your budget"
)

for keys in svb.keys():
  #def declare_var():
    globals()[keys] = st.selectbox( keys , sorted(list(svb[keys])), placeholder = keys)
  #declare_var()

features = [company, product, typename, inches, screenresolution, cpu, ram, memory, gpu, opsys, weight ]  
price= result(features)
if st.button("Click"):
  st.write(f"Your Budget should be £{round(price[0],-2):,}")
  st.write("Your specification are :- ")
  features_name = [x for x in svb.keys()]
  for f, fn in zip(features, features_name):
        st.write(f" {fn}: {f}")

