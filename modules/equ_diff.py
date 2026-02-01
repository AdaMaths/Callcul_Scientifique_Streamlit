import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def euler(phi, t0, tf, N, y0):
    t = np.linspace(t0, tf, N+1)
    h = (tf - t0)/N
    y = np.zeros(N+1)
    y[0] = y0
    for i in range(N):
        y[i+1] = y[i] + h*phi(t[i], y[i])
    return t, y

def app():
    st.header("📉 Équations Différentielles")

    eq = st.text_input("y' =", "y*np.sin(t)")
    t0 = st.number_input("t0", value=0.0)
    tf = st.number_input("tf", value=5.0)
    y0 = st.number_input("y0", value=1.0)
    N = st.slider("N", 10, 1000, 200)

    if st.button("Résoudre"):
        phi = lambda t, y: eval(eq)

        t, y = euler(phi, t0, tf, N, y0)

        fig, ax = plt.subplots()
        ax.plot(t, y)
        ax.set_title("Euler explicite")
        ax.grid(True)

        st.pyplot(fig)
