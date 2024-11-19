import streamlit as st
from net_calc import calculate

st.header("CALCULATIONS WITH PANDAPOWER")

results = calculate()

st.write(results[0])
st.write(results[1])