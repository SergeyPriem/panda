import streamlit as st

def ptotection_rule():

    st.text("60364-4-41 © IEC:2005")
    st.text("""411.4.4 The characteristics of the protective devices (see 411.4.5) and the circuit  impedances shall fulfil the following requirement:""")
    st.latex(r'Z_s * I_a \leq U_o')
    st.text("""where:\n
    Zs is the impedance in ohms (Ω) of the fault loop comprising\n
    – the source, \n
    – the line conductor up to the point of the fault, and \n
    – the protective conductor between the point of the fault and the source; \n
    Ia is the current in amperes (A) causing the automatic operation of the disconnecting device within the time specified in 411.3.2.2,or 411.3.2.3. When a residual current protective device (RCD) is used this current is the residual operating current providing disconnection in the time specified in 411.3.2.2,or 411.3.2.3: \n
    Uo is the nominal a.c. or d.c. line to earth voltage in volts (V).""")

    st.write("""*NOTE Where compliance with this subclause is provided by an RCD, the disconnecting times in accordance with /
Table 41.1 relate to prospective residual fault currents significantly higher than the rated residual operating current /
of the RCD (typically 5 I∆n).*""")