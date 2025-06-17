# ✈️ TripGuardian

> Your personal assistant for travel disruptions – real-time alerts, smart rerouting, and peace of mind when your journey hits turbulence.

---

## 🔍 Overview

**TripGuardian** is a real-time travel disruption assistant. It listens for flight delays, cancellations, or extreme weather and recommends smart, actionable alternatives—such as rebooking, switching airlines, or nearby hotels—so you’re never left stranded.

---

## 🎯 Features

- 🛰️ **Real-Time Flight Monitoring** via APIs (AviationStack, OpenSky)
- 🔁 **Rebooking Suggestions** across alliances and alternate airlines
- 💰 **Optimized Alternatives** from flight search APIs like Travelpayouts
- 🐳 Docker-ready for local and production deployment

---

## 📂 Project Structure

```bash
/tripguardian
├── app/                # FastAPI app and business logic
│   ├── main.py         # API routes
│   ├── services/       # External API integrations
│   └── models/         # Data models
├── data/               # Sample flight data, cache
├── tests/              # Unit tests
├── docs/               # Architecture, onboarding, usage
├── requirements.txt    # Python dependencies
└── README.md           # You are here
```

---

## 🧠 How it Works

1. **Input**: A user submits their flight itinerary and status (delay times, weather, etc.)
2. **Analysis**: The system predicts how disruptive the issue is using a trained ML model.
3. **Recommendation**: The engine suggests the best next step (rebook, wait, exit airport, etc.)
4. **Response**: FastAPI returns the plan to the user, in real-time.

---