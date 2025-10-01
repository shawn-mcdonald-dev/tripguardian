# ✈️ TripGuardian

> Your personal assistant for travel disruptions – real-time alerts, smart rerouting, and peace of mind when your journey hits turbulence.

---

## 🔍 Overview

**TripGuardian** is a real-time travel disruption assistant. It listens for flight delays, cancellations, or extreme weather and recommends smart, actionable alternatives—such as rebooking, switching airlines, or nearby hotels—so you’re never left stranded.

---

## 🧠 How it Works

1. **Input**: A user submits their flight itinerary and status (delay times, weather, etc.)
2. **Analysis**: The system predicts how disruptive the issue is using a trained ML model.
3. **Recommendation**: The engine suggests the best next step (rebook, wait, exit airport, etc.)
4. **Response**: FastAPI returns the plan to the user, in real-time.

---

## Getting Started

### Requirements
1. **[Download Docker Desktop](https://www.docker.com/get-started/)**

### Installation
```bash
# 1. Clone and setup
git clone https://github.com/shawn-mcdonald-dev/tripguardian.git
cd tripguardian

# 2. Configure environment
cp .env.example .env
# The .env file contains all necessary configuration for APIs

# 3. Add your API keys for AviationStack, RapidAPI, OpenAI_API
vi .env

# 4. Start all services
docker compose up --build -d

# 5. Verify backend works
curl http://localhost:8000
```

### Usage

Open Frontend (UI): `http://localhost:8501`
Open Backend (API): `http://localhost:8000`

Sam Persinger