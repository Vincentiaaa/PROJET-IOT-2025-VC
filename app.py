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

page = st.sidebar.radio("Navigate", ["Home","Weapon list", "Search", "Fun facts"])

if page == "Home":
    st.title("Welcome in DS3 Weapons !")
    if st.button("How Many Weapons are there ?"):
        much = ds3["Name"]
        total = much.count()
        st.write(f"There are {total} Weapons in Dark Souls 3 !")
        st.image("https://p325k7wa.twic.pics/high/dark-souls/dark-souls-2/00-page-setup/ds2_game-thumbnail.jpg?twic=v1/resize=760/step=10/quality=80", caption = "image dark souls 2")






elif page == "Weapon list":
    st.title("Dark souls 3 weapons list :")
    st.dataframe(ds3)
elif page == "Search":
    st.title("Searching something ? Check out our recommandations :")
    if st.button("10 Best Fire Weapons"):
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
    if st.button("10 Best PHY Weapons"):
        bestphy = ds3.sort_values(by="Physical Damage", ascending=False).iloc[:10]
        st.write(bestphy.loc[:, ["Name", "Physical Damage"]])
        bestphy2 = ds3.sort_values(by="Physical Damage", ascending=True).iloc[-10:]
        fig, ax = plt.subplots()
        plt.title("10 Best Physical Damage Weapons in Dark Souls 3", color = "blue")
        ax.plot(bestphy2["Physical Damage"], bestphy2["Name"], marker ='D', linestyle = ':', color = "black")
        ax.set_xlabel("PHY Damage", color = "brown")
        ax.set_ylabel("Item Name", color = "green")
        plt.grid(True)
        st.pyplot(fig)
    if st.button("10 Best Magic Weapons"):
        bestmag = ds3.sort_values(by="Magic Damage", ascending=False).iloc[:10]
        st.write(bestmag.loc[:, ["Name", "Magic Damage"]])
        bestmag2 = ds3.sort_values(by="Magic Damage", ascending=True).iloc[-10:]
        fig, ax = plt.subplots()
        plt.title("10 Best Magic Damage Weapons in Dark Souls 3", color = "blue")
        ax.plot(bestmag2["Magic Damage"], bestmag2["Name"], marker ='D', linestyle = ':', color = "black")
        ax.set_xlabel("Magic Damage", color = "blue")
        ax.set_ylabel("Item Name", color = "green")
        plt.grid(True)
        st.pyplot(fig)
    if st.button("5 Best Lightning Weapons"):
        bestlig = ds3.sort_values(by="Lightning Damage", ascending=False).iloc[:5]
        st.write(bestlig.loc[:, ["Name", "Lightning Damage"]])
        bestlig2 = ds3.sort_values(by="Lightning Damage", ascending=True).iloc[-5:]
        fig, ax = plt.subplots()
        plt.title("5 Best Lightning Damage Weapons in Dark Souls 3", color = "blue")
        ax.plot(bestlig2["Lightning Damage"], bestlig2["Name"], marker ='D', linestyle = ':', color = "black")
        ax.set_xlabel("Lightning Damage", color = "yellow")
        ax.set_ylabel("Item Name", color = "green")
        plt.grid(True)
        st.pyplot(fig)
elif page == "Fun facts":
    if st.button("Let's count all weight weapons !"):
        wei = ds3["Weight"].value_counts()
        st.write(wei)
    if st.button("Then , how much weight do we obtain if we add everything ?"):
        weitotal = ds3["Weight"].sum()
        st.write(f"Weight is {weitotal} kilos. Damn it's Really heavy !")




