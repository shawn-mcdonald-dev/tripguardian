# ✈️ TripGuardian

> Your personal assistant for travel disruptions – real-time alerts, smart rerouting, and peace of mind when your journey hits turbulence.

---

## 🔍 Overview

TripGuardian is an intelligent travel companion that proactively monitors your flight itinerary and helps you respond to real-time disruptions like delays, missed connections, and severe weather. Whether you're a digital nomad, business traveler, or just trying to get home on time—TripGuardian is your fallback plan, always.

---

## 🎯 MVP Features

- 🚦 Classify travel disruptions as **minor**, **major**, or **critical**
- 🔁 Suggest actions: **wait**, **rebook**, **book hotel**, or **reroute**
- 📡 Fetch and parse structured trip data (manual or from APIs)
- 🔍 Use ML + rule-based recommendations
- 📊 Offer API interface (via FastAPI)

---

## 🛠️ Tech Stack

| Layer | Tool |
|-------|------|
| Backend API | FastAPI |
| ML/Inference | Scikit-learn, Pandas |
| Data Store | CSV / SQLite (MVP) |
| Containerization | Docker |
| Tests | Pytest |
| Future | MLflow, Cloud Deploy, Streamlit dashboard |

---

## 🧠 How it Works

1. **Input**: A user submits their flight itinerary and status (delay times, weather, etc.)
2. **Analysis**: The system predicts how disruptive the issue is using a trained ML model.
3. **Recommendation**: The engine suggests the best next step (rebook, wait, exit airport, etc.)
4. **Response**: FastAPI returns the plan to the user, in real-time.

---

## 🧪 Example Input (POST `/analyze_disruption`)

```json
{
  "trip_id": "abc123",
  "flights": [
    {"from": "JFK", "to": "LHR", "delay_mins": 0},
    {"from": "LHR", "to": "BER", "delay_mins": 95}
  ],
  "weather": {
    "LHR": "Fog",
    "BER": "Clear"
  },
  "current_location": "LHR"
}

