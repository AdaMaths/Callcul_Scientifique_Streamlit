import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def app():
    st.header("🎛️ Automatique")

    Kp = st.number_input("Kp", 1.0)
    Ki = st.number_input("Ki", 0.0)
    Kd = st.number_input("Kd", 0.0)

    if st.button("Simuler PID"):
        s = signal.TransferFunction.s
        G = 1/(s**2 + 3*s + 2)
        PID = Kp + Ki/s + Kd*s
        H = signal.feedback(PID*G, 1)

        t, y = signal.step(H)
        fig, ax = plt.subplots()
        ax.plot(t, y)
        ax.grid(True)
        st.pyplot(fig)