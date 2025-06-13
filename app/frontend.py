import streamlit as st
from app.logic import get_disruption_level, suggest_action

st.set_page_config(page_title="TripGuardian", page_icon="🛫")
st.title("🛫 TripGuardian – Travel Disruption Assistant")

st.subheader("Enter your flight details")

# Input form
flight_number = st.text_input("Flight Number", placeholder="e.g. AA123")
departure_airport = st.text_input("Departure Airport", placeholder="e.g. JFK")
arrival_airport = st.text_input("Arrival Airport", placeholder="e.g. LAX")
departure_time = st.text_input("Scheduled Departure Time", placeholder="e.g. 2025-06-10T14:30")
delay_minutes = st.number_input("Current Delay (in minutes)", min_value=0, value=0)

if st.button("Check Disruption"):
    if delay_minutes is not None:
        level = get_disruption_level(delay_minutes)
        action = suggest_action(level)

        st.success(f"✈️ Disruption Level: **{level}**")
        st.info(f"📌 Recommended Action: {action}")
    else:
        st.error("Please enter all required fields.")
