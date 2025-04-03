import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

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
    ds3graph = ds3[["Fire Damage", "Magic Damage"]]
    st.scatter_chart(ds3graph)


elif page == "Toutes les armes":
    st.title("Liste des armes de Dark Souls 3 :")
    st.dataframe(ds3)
elif page == "Recherche spécifique":
    st.title("Vous cherchez quelque chose ? Regardez nos catégories :")
    if st.button("10 Meilleures armes de feu"):
        bestfire = ds3.sort_values(by="Fire Damage", ascending=False).iloc[:10]
        st.write(bestfire.loc[:, ["Name", "Fire Damage"]])
        bestfire2 = ds3.sort_values(by="Fire Damage", ascending=True).iloc[-10:]
        fig, ax = plt.subplots()
        plt.title("10 Best Fire Damage Weapons in Dark Souls 3", color = "blue")
        ax.plot(bestfire2["Fire Damage"], bestfire2["Name"], marker ='D', linestyle = ':', color = "black")
        ax.set_xlabel("Fire Damage", color = "red")
        ax.set_ylabel("Item Name", color = "green")
        plt.grid(True)
        st.pyplot(fig)
    if st.button("10 Meilleures armes physiques"):
        bestphy = ds3.sort_values(by="Physical Damage", ascending=False).iloc[:10]
        st.write(bestphy.loc[:, ["Name", "Physical Damage"]])
    if st.button("10 Meilleures armes magiques"):
        bestmag = ds3.sort_values(by="Magic Damage", ascending=False).iloc[:10]
        st.write(bestmag.loc[:, ["Name", "Magic Damage"]])
    if st.button("10 Meilleures armes électiques"):
        bestlig = ds3.sort_values(by="Lightning Damage", ascending=False).iloc[:10]
        st.write(bestlig.loc[:, ["Name", "Lightning Damage"]])
    if st.button("10 Meilleures armes occultes"):
        bestdark = ds3.sort_values(by="Dark Damage", ascending=False).iloc[:10]
        st.write(bestdark.loc[:, ["Name", "Dark Damage"]])


