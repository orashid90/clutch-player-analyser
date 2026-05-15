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

    col1, col2 = st.columns(2)

    player_names = list(data["players"].keys())

    player1_data = data["players"][player_names[0]]

    player2_data = data["players"][player_names[1]]

    with col1: 

        st.header(player_names[0])

        st.metric(
            "Clutch Rating",
            player1_data["clutch_rating"]
        )

        st.metric(
            "Average Clutch Score",
            player1_data["average_clutch_score"]
        )

        st.write(
            "Profile:",
            player1_data["profile"]["label"]
        )

        st.write(
            "Best Moment: ",
            f"{player1_data['best_moment']['minute']}'"
            f" - "
            f"{player1_data['best_moment']['moment_type']}"
        )

    with col2: 

        st.header(player_names[1])

        st.metric(
            "Clutch Rating",
            player2_data["clutch_rating"]
        )

        st.metric(
            "Average Clutch Score",
            player2_data["average_clutch_score"]
        )

        st.write(
            "Profile:",
            player2_data["profile"]["label"]
        )

        st.write(
            "Best Moment: ",
            f"{player2_data['best_moment']['minute']}'"
            f" - "
            f"{player2_data['best_moment']['moment_type']}"
        )