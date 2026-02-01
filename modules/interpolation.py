import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def lagrange(x, xi, yi):
    L = np.zeros_like(x)
    for i in range(len(xi)):
        li = np.ones_like(x)
        for j in range(len(xi)):
            if i != j:
                li *= (x - xi[j]) / (xi[i] - xi[j])
        L += yi[i] * li
    return L

def app():
    st.header("📈 Interpolation")

    func_str = st.text_input("f(x)", "np.cos(2*np.pi*x)")
    a = st.number_input("a", value=0.0)
    b = st.number_input("b", value=1.0)
    N = st.slider("Nombre de points", 2, 20, 5)

    method = st.selectbox("Méthode", ["Lagrange", "Newton (à ajouter)"])

    if st.button("Calculer"):
        f = lambda x: eval(func_str)
        xi = np.linspace(a, b, N)
        yi = f(xi)

        x = np.linspace(a, b, 500)

        fig, ax = plt.subplots()
        ax.scatter(xi, yi, color="red")

        if method == "Lagrange":
            ax.plot(x, lagrange(x, xi, yi))

        ax.grid(True)
        st.pyplot(fig)
