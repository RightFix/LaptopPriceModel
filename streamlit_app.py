import streamlit as st
#from ipynb.fs.full.main import result, svb
from man import svb, result

st.title("Laptop Prediction Model App")
st.write(
    "Select your laptop specification So you would know your budget"
)

company = st.selectbox( "Company" , sorted(list(svb["company"])),  placeholder = "Company")
product= st.selectbox( "Product" , sorted(list(svb["product"])),  placeholder = "Product")
typename = st.selectbox( "Type Name", sorted(list(svb["typename"])),  placeholder = "Type Name")
inches = st.selectbox( "Inches", sorted(list(svb["inches"])), placeholder = "Inches")
screenresolution =  st.selectbox( "Screen Resolution" , [""] +sorted(list(svb["screenresolution"])), placeholder = "Screen Resolution")
cpu= st.selectbox( "CPU", sorted(list(svb["cpu"])), placeholder = "CPU")
ram = st.selectbox( "RAM", sorted(list(svb["ram"])),placeholder = "RAM")
memory = st.selectbox( "Memory",  sorted(list(svb["memory"])), placeholder = "Memory",)
gpu = st.selectbox( "GPU" , sorted(list(svb["gpu"])),  placeholder ="GPU")
opsys= st.selectbox( "Operating System" , [""] +  sorted(list(svb["opsys"])),  placeholder ="Operating System")
weight= st.selectbox( "Weight" , [""] + sorted(list(svb["weight"])), placeholder ="Weight")

features = [company, product, typename, inches, screenresolution, cpu, ram, memory, gpu, opsys, weight ]  
price= result(features)
if st.button("Click"):
  st.write(f"Your Budget should be £{round(price[0],-2):,}")
  st.write(f"Your Budget should be £{features}")

