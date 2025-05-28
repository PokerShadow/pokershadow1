
import streamlit as st
import matplotlib.pyplot as plt
import os
import json
from datetime import date

# Aseta tumma teema automaattisesti
st.set_page_config(page_title="PokerShadow", layout="centered")

DATA_FILE = "players.json"

# Lue pelaajat JSON-tiedostosta
def load_players():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

# Tallenna pelaajat JSON-tiedostoon
def save_players(players):
    with open(DATA_FILE, "w") as f:
        json.dump(players, f, indent=4)

# Alustetaan
if "players" not in st.session_state:
    st.session_state.players = load_players()

# TUMMA TEEMA
st.markdown("""
    <style>
    body, .stApp {
        background-color: #121212;
        color: #f0f0f0;
    }
    .stTextInput > label, .stNumberInput > label {
        color: #f0f0f0;
    }
    </style>
""", unsafe_allow_html=True)

# APP OTSIKKO
st.title("🃏 PokerShadow")

# ADMIN - Lisää pelaaja
with st.sidebar:
    st.title("➕ Add Player (Admin)")
    with st.form("add_player_form"):
        nickname = st.text_input("Nickname")
        tournaments = st.number_input("Tournaments played", min_value=0)
        avg_roi = st.number_input("Average ROI (%)", format="%.1f")
        total_profit = st.number_input("Total profit ($)", min_value=0)
        avg_finish = st.text_input("Average finish (e.g. 12th)")
        avg_buyin = st.number_input("Average buy-in ($)", min_value=0)
        biggest_cash = st.number_input("Biggest cash ($)", min_value=0)
        latest_tournament = st.date_input("Latest tournament", value=date.today())
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
                save_players(st.session_state.players)
                st.success(f"✅ Player '{nickname}' added and saved.")
            except Exception as e:
                st.error(f"Error parsing graph data: {e}")

# HAKU
username = st.text_input("🔎 Search player by nickname").strip()

if username:
    player = st.session_state.players.get(username)
    if player:
        st.header(f"📄 Profile: {username}")
        col1, col2, col3 = st.columns(3)
        col1.metric("Tournaments", player['tournaments'])
        col2.metric("Avg ROI", f"+{player['avg_roi']}%")
        col3.metric("Total Profit", f"${player['total_profit']:,}")

        st.subheader("📈 Profit Chart")
        fig, ax = plt.subplots()
        ax.plot(player['graph'], linewidth=2, color="cyan")
        ax.set_ylabel("Profit $")
        st.pyplot(fig)

        st.subheader("📋 Details")
        st.markdown(f"- **Average Finish:** {player['avg_finish']}")
        st.markdown(f"- **Average Buy-in:** ${player['avg_buyin']}")
        st.markdown(f"- **Biggest Cash:** ${player['biggest_cash']}")
        st.markdown(f"- **Latest Tournament:** {player['latest_tournament']}")
    else:
        st.error("❌ Player not found.")
else:
    st.info("Enter a nickname to search for a poker profile.")
