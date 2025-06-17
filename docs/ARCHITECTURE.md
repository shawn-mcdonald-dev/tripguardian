## TripGuardian Architecture

### Components:
- `main.py`: FastAPI entrypoint.
- `flight_status.py`: Interfaces with AviationStack for flight tracking.
- `flight_search.py`: Finds alternate flights via Kiwi.

### Data Flow:
1. User inputs flight (UI/API)
2. System polls for disruption
3. If disrupted → call rebooking engine
4. Rebooking engine returns Option A (same alliance), Option B (other)

---

### Updates 06/13/2025
- Working FastAPI backend

**Next Steps**
- Call APIs for real time flight data

#### A. Flight Monitoring Workflow
1. User inputs flight info (or forwards confirmation email).
2. You store flight number + date.
3. Periodically poll flight status API.
4. If delay > threshold OR status == cancelled, trigger rebooking logic.

#### B. Rebooking Logic
1. Match original airline to its alliance.
2. Query available flights to the same destination (via Amadeus, Skyscanner).
3. Filter:
- Flights after current time.
- Same alliance → Option A.
- Different carrier → Option B.

**Example outputs**
```
Your next flight won’t wait.
Option A: Rebook via same alliance (Airline: Lufthansa, Departs: 17:00)
Option B: Switch to different carrier (Delta, Departs: 17:30)
```

---