import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def app():
    st.header("📉 Optimisation")

    f_str = st.text_input("f(x)", "x**2 - 4*x + 3")
    x0 = st.number_input("x0", 0.0)
    xmin = st.number_input("xmin", -10.0)
    xmax = st.number_input("xmax", 10.0)

    if st.button("Calculer"):
        f = lambda x: eval(f_str, {"__builtins__": {}}, {"x": x, "np": np})
        res = minimize(f, x0, bounds=[(xmin, xmax)])

        x = np.linspace(xmin, xmax, 400)
        y = f(x)

        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.scatter(res.x, f(res.x), color="red")
        st.pyplot(fig)