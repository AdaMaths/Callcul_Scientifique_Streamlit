import streamlit as st

st.set_page_config(page_title="Calcul Scientifique", layout="wide")

st.sidebar.title("📐 Menu")
dark = st.sidebar.toggle("🌙 Mode sombre")

if dark:
    st.markdown("""
    <style>
    body, .stApp { background-color:#0e1117; color:#fafafa; }
    </style>
    """, unsafe_allow_html=True)

menu = st.sidebar.selectbox("Choisir un module", [
    "Optimisation",
    "Automatique"
    "gaussian_laser",
    "equ_diff"
    "interpolation",
    ])

if menu == "Optimisation":
    from modules.optimisation import app
    app()

elif menu == "equ_diff":
    from modules.equ_diff import app
    app()

elif menu == "interpolation":
    from modules.interpolation import app
    app()

elif menu == "gaussian_laser":
    from modules.gaussian_laser import app
    app()



st.markdown("""<hr><center><b>Plateforme de Calcul Scientifique</b><br>
Développée par <b>Adama Gueye</b> © 2026</center>""", unsafe_allow_html=True)
