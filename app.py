import streamlit as st
import pandas as pd

ds3 = pd.read_csv("DS3_weapon.csv")

page = st.sidebar.radio("Navigation", ["Accueil","Toutes les armes"])

if page == "Accueil":
    st.title("Bienvenue sur DS3 Weapons !")
    st.image("https://p325k7wa.twic.pics/high/dark-souls/dark-souls-2/00-page-setup/ds2_game-thumbnail.jpg?twic=v1/resize=760/step=10/quality=80", caption = "image dark souls 2")
elif page == "Toutes les armes":
    st.write("Liste des armes de Dark Souls 3 :")
    del ds3["Stability"]
    del ds3["Sell Price"]
    del ds3["Critical"]
    st.dataframe(ds3)
