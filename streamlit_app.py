import streamlit as st
#from ipynb.fs.full.main import result, svb
from man import svb, result

st.title("Laptop Prediction Model App")
st.write(
    "Select your laptop specification So you would know your budget"
)

company = st.selectbox( "Company :" , sorted(list(svb[str(company)])), index = None, placeholder = "Company")
product = st.selectbox( "Product :" , sorted(list(svb[str(product)])), index = None, placeholder = "Product")
typename = st.selectbox( "Type Name", sorted(list(svb[str(typename)])), index = None, placeholder = "Type Name")
screeenresoluttion =  st.selectbox( "Screen Resolution" , sorted(list(svb[str(screeenresoluttion)])), index = None, placeholder = "Screen Resolution")
cpu= st.selectbox( "CPU", sorted(list(svb[str(cpu)])), index = None, placeholder = "CPU")
ram = st.selectbox( "RAM", sorted(list(svb[str(ram)])), index = None, placeholder = options,)
company = st.selectbox( options.capitalize() , sorted(list(svb[str(company)])), index = None, placeholder = options,)
company = st.selectbox( options.capitalize() , sorted(list(svb[str(company)])), index = None, placeholder = options,)

features = [company, product, typename, screeenresoluttion, cpu, ram, , memory, gpu, opsys, weight ]  
price= result(features)
if st.button("Click"):
  st.write(f"Your Budget should be £{price[0]}")
  st.write(f"Your Budget should be £{features}")

