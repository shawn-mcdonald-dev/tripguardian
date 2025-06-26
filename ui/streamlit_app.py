import streamlit as st
import requests
import os

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
API_URL = f"{API_BASE_URL}/v1/reroute"


st.set_page_config(page_title="TripGuardian", page_icon="✈️")
st.title("🧭 TripGuardian Travel Assistant")

st.markdown("Get personalized help during travel delays or cancellations.")

with st.form("reroute_form"):
    origin = st.text_input("Departure Airport Code (e.g. JFK)")
    destination = st.text_input("Arrival Airport Code (e.g. LHR)")
    delay_minutes = st.number_input("Delay (in minutes)", min_value=0, value=0)
    weather_conditions = st.text_input("Weather Conditions (e.g. fog, storm)")
    user_priority = st.selectbox("Your Priority", ["minimize cost", "minimize delay", "comfortable option"])
    
    submitted = st.form_submit_button("Get Recommendation")

    if submitted:
        if not origin or not destination:
            st.error("Please fill out all fields.")
        else:
            payload = {
                "origin": origin,
                "destination": destination,
                "delay_minutes": delay_minutes,
                "weather_conditions": weather_conditions,
                "user_priority": user_priority
            }

            try:
                with st.spinner("Thinking..."):
                    st.code(f"Sending POST to {API_URL} with: {payload}")
                    response = requests.post(API_URL, json=payload)
                    
                    st.write(f"Status Code: {response.status_code}")
                    st.write(f"Raw Response: {response.text}")

                    if response.status_code == 200:
                        st.success("TripGuardian's Recommendation:")
                        st.write(response.json()["recommendation"])
                    else:
                        st.error(f"Backend returned error: {response.status_code}")
            except Exception as e:
                st.error(f"Error: {e}")
