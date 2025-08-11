import streamlit as st
#from ipynb.fs.full.main import result, svb
from man import svb, result

st.title("Laptop Prediction Model App")
st.write(
    "Select your laptop specification So you would know your budget"
)

company = st.selectbox( "Company :" , sorted(list(svb[str(company)])), index = None, placeholder = options,)
product = st.selectbox( "Product :" , sorted(list(svb[str(product)])), index = None, placeholder = options,)
company = st.selectbox( options.capitalize() , sorted(list(svb[str(company)])), index = None, placeholder = options,)
company = st.selectbox( options.capitalize() , sorted(list(svb[str(company)])), index = None, placeholder = options,)
company = st.selectbox( options.capitalize() , sorted(list(svb[str(company)])), index = None, placeholder = options,)
company = st.selectbox( options.capitalize() , sorted(list(svb[str(company)])), index = None, placeholder = options,)
company = st.selectbox( options.capitalize() , sorted(list(svb[str(company)])), index = None, placeholder = options,)
company = st.selectbox( options.capitalize() , sorted(list(svb[str(company)])), index = None, placeholder = options,)

features = [company, product, typename, screeenresoluttion, cpu, ram, , memory, gpu, opsys, weight ]  
price= result(features)
if st.button("Click"):
  st.write(f"Your Budget should be £{price[0]}")
  st.write(f"Your Budget should be £{features}")

