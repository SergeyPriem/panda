import streamlit as st

from iec import (protection_rule_1, protection_rule_2, protection_rule_3, protection_rule_4,
                 protection_rule_5, protection_rule_6, protection_rule_7)
from net_calc import calculate

with st.sidebar:
    options = ["Calculations", "Codes"]
    selection = st.segmented_control(
        "Directions", options, selection_mode="single"
    )


if selection is None:
    st.header("Select the option")
    st.write("and Good Luck!")
else:
    st.header(selection)
    

if selection == "Calculations":

    st.subheader("Initial Data")
    st.subheader("GRID")
    st.subheader("Buses")
    st.subheader("Lines")
    st.subheader("Transformers")
    st.divider()

    st.subheader("Results")
    results = calculate()
    st.subheader("Voltages")

    st.write(results[0])
    st.subheader("Currents")
    st.write(results[1])
    st.subheader("Lines")
    st.write(results[2].line)

    if st.button('Show Net Dictionary'):
        st.write(results[2])


if selection == "Codes":
    protection_rule_1()
    st.divider()
    protection_rule_2()
    st.divider()
    protection_rule_3()
    st.divider()
    protection_rule_4()
    st.divider()
    protection_rule_5()
    st.divider()
    protection_rule_6()
    st.divider()
    protection_rule_7()

