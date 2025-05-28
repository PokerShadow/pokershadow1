
import streamlit as st
import matplotlib.pyplot as plt

# Session-state player storage
if 'players' not in st.session_state:
    st.session_state.players = {
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

st.title("PokerShadow 🃏")

st.sidebar.title("➕ Add Player (Admin)")
with st.sidebar.form("add_player_form"):
    nickname = st.text_input("Nickname")
    tournaments = st.number_input("Tournaments played", min_value=0)
    avg_roi = st.number_input("Average ROI (%)", format="%.1f")
    total_profit = st.number_input("Total profit ($)", min_value=0)
    avg_finish = st.text_input("Average finish (e.g. 12th)")
    avg_buyin = st.number_input("Average buy-in ($)", min_value=0)
    biggest_cash = st.number_input("Biggest cash ($)", min_value=0)
    latest_tournament = st.date_input("Latest tournament")
    graph_data = st.text_input("Profit graph data (comma-separated numbers)")

    submitted = st.form_submit_button("Add Player")
    if submitted and nickname:
        try:
            graph = [int(x.strip()) for x in graph_data.split(",") if x.strip().isdigit()]
            st.session_state.players[nickname] = {
                "tournaments": tournaments,
                "avg_roi": avg_roi,
                "total_profit": total_profit,
                "avg_finish": avg_finish,
                "avg_buyin": avg_buyin,
                "biggest_cash": biggest_cash,
                "latest_tournament": str(latest_tournament),
                "graph": graph
            }
            st.success(f"✅ Player '{nickname}' added.")
        except Exception as e:
            st.error(f"Error parsing graph data: {e}")

# Player search
username = st.text_input("Search player by nickname").strip()

if username:
    player = st.session_state.players.get(username)
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
