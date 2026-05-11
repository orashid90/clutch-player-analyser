import streamlit as st
import requests

st.title("⚽ Premier League Clutch Player Dashboard")

st.write("Compare how clutch Premier League attackers and midfielders are.")

player1 = st.text_input("Enter Player 1")

player2 = st.text_input("Enter Player 2")

if st.button("Compare Players"):
    url = f"http://127.0.0.1:8000/compare/?player1={player1}&player2={player2}"

    response = requests.get(url)

    data = response.json()

    st.write(data)

    st.subheader(data["summary"])

    st.write("🏆 Winner:", data["winner"])

    st.write(data["insight"])