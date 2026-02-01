import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def app():
    st.header("🔵 Profil Gaussien")

    amplitude = st.number_input("Amplitude", value=1.0)
    sigma = st.number_input("Sigma", value=1.0)

    if st.button("Générer"):
        x = np.linspace(-10, 10, 1000)
        y = amplitude * np.exp(-(x**2)/(2*sigma**2))

        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title("Profil Gaussien")
        ax.set_xlabel("x")
        ax.set_ylabel("Amplitude")
        ax.grid(True)

        st.pyplot(fig)
