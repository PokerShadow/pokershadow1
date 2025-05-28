import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("PokerShadow 🃏")

username = st.text_input("Search player")

sample_data = {
    "username": "P1ayer56",
    "tournaments": 1254,
    "avg_roi": 12.5,
    "total_profit": 32580,
    "avg_finish": "13th",
    "avg_buyin": 55,
    "biggest_cash": 8120,
    "latest_tournament": "2024-03-15",
    "graph": [0, 300, 280, 500, 470, 900, 850, 950, 1600, 1400, 1900, 2400, 2500, 3100]
}

if username:
    st.header(f"Profile: {sample_data['username']}")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Tournaments", sample_data['tournaments'])
    col2.metric("Avg ROI", f"+{sample_data['avg_roi']}%")
    col3.metric("Total Profit", f"${sample_data['total_profit']:,}")
    
    st.subheader("Profit Chart")
    fig, ax = plt.subplots()
    ax.plot(sample_data['graph'], linewidth=2)
    ax.set_ylabel("Profit $")
    st.pyplot(fig)
    
    st.subheader("Details")
    st.markdown(f"- **Average Finish:** {sample_data['avg_finish']}")
    st.markdown(f"- **Average Buy-in:** ${sample_data['avg_buyin']}")
    st.markdown(f"- **Biggest Cash:** ${sample_data['biggest_cash']}")
    st.markdown(f"- **Latest Tournament:** {sample_data['latest_tournament']}")
else:
    st.info("Search for a player to see stats.")
