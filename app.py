import streamlit as st
import pandas as pd

ds3 = pd.read_csv("DS3_weapon.csv")
del ds3["Stability"]
del ds3["Sell Price"]
del ds3["Critical"]
ds3[['Physical Damage', 'Magic Damage', 'Fire Damage','Lightning Damage', 'Dark Damage']] = ds3["Damage"].str.split('/', expand=True)
del ds3["Damage"]

page = st.sidebar.radio("Navigation", ["Accueil","Toutes les armes", "Recherche spécifique"])

if page == "Accueil":
    st.title("Bienvenue sur DS3 Weapons !")
    st.image("https://p325k7wa.twic.pics/high/dark-souls/dark-souls-2/00-page-setup/ds2_game-thumbnail.jpg?twic=v1/resize=760/step=10/quality=80", caption = "image dark souls 2")
elif page == "Toutes les armes":
    st.title("Liste des armes de Dark Souls 3 :")
    st.dataframe(ds3)
elif page == "Recherche spécifique":
    st.title("Vous cherchez quelque chose ? Regardez nos catégories :")
    if st.button("10 Meilleures armes de feu"):
        bestfire = ds3.loc[ds3['Fire Damage']].max()
        st.write(bestfire)


