import streamlit as st
import requests
import pandas as pd

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
        
        st.write("🔥 Best Moment")

        st.write(
            f"{player1_data['best_moment']['minute']}' "
            f"{player1_data['best_moment']['moment_type']}"
        )

        st.caption(
            f"Clutch Score: "
            f"{player1_data['best_moment']['clutch_score']}"
        )


        comfort = player1_data["profile"]["comfort_events"]

        neutral = player1_data["profile"]["neutral_events"]

        clutch = player1_data["profile"]["clutch_events"]

        total = player1_data["profile"]["total_events"]

        st.write(f"🟥 Comfort: {comfort}")

        st.progress(comfort / total)

        st.write(f"🟨 Neutral: {neutral}")

        st.progress (neutral / total)

        st.write(f"🟩 Clutch: {clutch}")

        st.progress(clutch / total)

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

        st.write("🔥 Best Moment")

        st.write(
            f"{player2_data['best_moment']['minute']}' "
            f"{player2_data['best_moment']['moment_type']}"
        )

        st.caption(
            f"Clutch Score: "
            f"{player2_data['best_moment']['clutch_score']}"
        )

        comfort2 = player2_data["profile"]["comfort_events"]

        neutral2 = player2_data["profile"]["neutral_events"]

        clutch2 = player2_data["profile"]["clutch_events"]

        total2 = player2_data["profile"]["total_events"]

        st.write(f"🟥 Comfort: {comfort2}")

        st.progress(comfort2 / total2)

        st.write(f"🟨 Neutral: {neutral2}")

        st.progress (neutral2 / total2)

        st.write(f"🟩 Clutch: {clutch2}")

        st.progress(clutch2 / total2)

    chart_data = pd.DataFrame({
        "Player": player_names,
        "Clutch Rating": [
            player1_data["clutch_rating"],
            player2_data["clutch_rating"]
        ]
    })

    st.subheader("Clutch Rating Comparison")

    st.bar_chart(
        chart_data.set_index("Player")
    )
