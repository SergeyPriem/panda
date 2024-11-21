import streamlit as st

def ptotection_rule_1():

    st.markdown("<b>60364-4-41 © IEC:2005</b>", unsafe_allow_html=True)
    st.text("""411.4.4 The characteristics of the protective devices (see 411.4.5) and the circuit  impedances shall fulfil the following requirement:""")
    st.latex(r'Z_S * I_a \leq U_o')
    st.text("""where:
    
    Zs is the impedance in ohms (Ω) of the fault loop comprising
    
    – the source, 
    
    – the line conductor up to the point of the fault, and 
    
    – the protective conductor between the point of the fault and the source; 
    
    Ia is the current in amperes (A) causing the automatic operation of the disconnecting device within 
    the time specified in 411.3.2.2,or 411.3.2.3. When a residual current protective device (RCD) is used 
    this current is the residual operating current providing disconnection in the time specified in 
    411.3.2.2,or 411.3.2.3: \n
    Uo is the nominal a.c. or d.c. line to earth voltage in volts (V).""")

    st.write("""*NOTE Where compliance with this subclause is provided by an RCD, the disconnecting times in 
    accordance with Table 41.1 relate to prospective residual fault currents significantly higher than 
    the rated residual operating current of the RCD (typically 5 I∆n).*""")

    st.markdown("""<b>411.4.5</b> In TN systems, the following protective devices may be used for fault protection
(protection against indirect contact):

– overcurrent protective devices;

– residual current protective devices (RCDs).

<i>NOTE 1 Where an RCD is used for fault protection the circuit should also be protected by an overcurrent
protective device in accordance with IEC 60364-4-43.
A residual current protective device (RCD) shall not be used in TN-C systems.
Where an RCD is used in a TN-C-S system, a PEN conductor shall not be used on the load
side. The connection of the protective conductor to the PEN conductor shall be made on the
source side of the RCD.

NOTE 2 Where discrimination between RCDs is necessary, see 535.3 of IEC 60364-5-53.</i>""", unsafe_allow_html=True)


def ptotection_rule_2():
    st.markdown("<b>60364-5-54 © IEC:2011</b>", unsafe_allow_html=True)

    st.markdown("""<b>542.1.1</b> The earthing arrangements may be used jointly or separately 
    for protective and functional purposes according to the requirements of the electrical installation. 
    <u>The requirements for protective purposes shall always take precedence.</u>""", unsafe_allow_html=True)


def ptotection_rule_3():
    st.markdown("<b>IEEE Std 80-2000</b> (Revision of IEEE Std 80-1986)", unsafe_allow_html=True)
    st.markdown("""<b>14.1 Usual requirements</b>
    
A good grounding system provides a low resistance to remote earth in order to minimize the GPR. For most
transmission and other large substations, the ground resistance is usually about 1 Ω or less. In smaller distribution 
substations, <u>the usually acceptable range is from 1 Ω to 5 Ω, depending on the local conditions.</u>""",
                unsafe_allow_html=True)
