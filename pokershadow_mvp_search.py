
import streamlit as st
import matplotlib.pyplot as plt

st.title("PokerShadow 🃏")

# Pelaajadatabase (simuloitu)
players = {
    "nikkim98": {
        "tournaments": 732,
        "avg_roi": 18.3,
        "total_profit": 17420,
        "avg_finish": "11th",
        "avg_buyin": 44,
        "biggest_cash": 4100,
        "latest_tournament": "2024-05-18",
        "graph": [0, 200, 350, 800, 760, 1300, 1100, 1800, 1900, 2600, 3100]
    },
    "Tinde_98": {
        "tournaments": 403,
        "avg_roi": 25.7,
        "total_profit": 12360,
        "avg_finish": "8th",
        "avg_buyin": 33,
        "biggest_cash": 2750,
        "latest_tournament": "2024-05-24",
        "graph": [0, 120, 300, 620, 580, 1020, 1200, 1700, 2100, 2700]
    }
}

# Haku
username = st.text_input("Search player by nickname (e.g. nikkim98, Tinde_98)").strip()

if username:
    player = players.get(username)
    if player:
        st.header(f"Profile: {username}")

        col1, col2, col3 = st.columns(3)
        col1.metric("Tournaments", player['tournaments'])
        col2.metric("Avg ROI", f"+{player['avg_roi']}%")
        col3.metric("Total Profit", f"${player['total_profit']:,}")

        st.subheader("Profit Chart")
        fig, ax = plt.subplots()
        ax.plot(player['graph'], linewidth=2)
        ax.set_ylabel("Profit $")
        st.pyplot(fig)

        st.subheader("Details")
        st.markdown(f"- **Average Finish:** {player['avg_finish']}")
        st.markdown(f"- **Average Buy-in:** ${player['avg_buyin']}")
        st.markdown(f"- **Biggest Cash:** ${player['biggest_cash']}")
        st.markdown(f"- **Latest Tournament:** {player['latest_tournament']}")
    else:
        st.error("Player not found.")
else:
    st.info("Enter a nickname to search for a poker profile.")
