# ⚽ Clutch Player Analyser

A football analytics project that measures how "clutch" Premier League attackers and midfielders are based on the importance and timing of their goals and assists.

The aim of the project is to go beyond raw goals and assists by analysing:

* when a player contributed
* the match situation at the time
* whether the contribution came under pressure
* whether the player consistently delivers in decisive moments

---

# 🚀 Project Vision

Traditional football statistics treat all goals equally.

This project attempts to answer questions such as:

* Is a player scoring when it actually matters?
* Does the player step up in high-pressure moments?
* Are they contributing in winning moments or comfortable situations?
* Who is truly the more clutch player?

The long-term goal is to evolve this into a full football analytics platform with:

* real match datasets
* opponent difficulty weighting
* advanced player comparisons
* visual dashboards
* deployment to the cloud
* automated testing and CI/CD

---

# 🧠 Current Features

## ✅ Clutch Scoring System

Each goal or assist is scored using two factors:

### 1. Match State Weighting

| Match Situation Before Goal | Score |
| --------------------------- | ----- |
| 3+ goals behind             | 1     |
| Already 2+ goals ahead      | 1     |
| Already 1 goal ahead        | 2     |
| 2 goals behind              | 2     |
| Equaliser                   | 3     |
| Goal to take the lead       | 4     |

---

### 2. Timing Weighting

| Match Minute | Score |
| ------------ | ----- |
| 0–45         | 1     |
| 45–75        | 2     |
| 75–90        | 3     |
| 90+          | 4     |

---

## ✅ Total Clutch Score

Each event receives a combined clutch score:

```python
clutch_score = game_state_score + timing_score
```

This creates a weighted scoring model where:

* late winners score highly
* low-pressure goals score lower

---

## ✅ Player Event Analysis

The API can:

* return all clutch events for a player
* identify their best clutch moment
* calculate average clutch score
* sort contributions by importance

---

## ✅ Comfort vs Clutch Profile

Players are categorised based on contribution patterns:

| Profile          | Meaning                                            |
| ---------------- | -------------------------------------------------- |
| Comfort Merchant | Majority of contributions in low-pressure moments  |
| Balanced         | Mix of clutch and lower-pressure contributions     |
| Clutch Player    | Majority of contributions in high-pressure moments |

---

## ✅ Player Comparison Engine

Players can be compared using:

* total clutch score
* average clutch score
* clutch rating
* best clutch moment
* contribution profile

A weighted `clutch_rating` metric combines:

* overall contribution volume
* average contribution quality

This helps prevent high-volume low-impact players from unfairly ranking above players with decisive match-winning contributions.

---

## ✅ FastAPI Backend

The backend is built using FastAPI and exposes endpoints for:

* player analysis
* comparison
* event retrieval

---

## ✅ Streamlit Dashboard

A basic frontend dashboard has been implemented using Streamlit.

Users can:

* enter player names
* compare players visually
* consume live API data from the FastAPI backend

---

# 🏗️ Project Structure

```text
Clutch Player Analyser/
│
├── app/
│   ├── main.py
│   ├── scoring.py
│   └── player_score.py
│
├── data/
│   └── player_data.csv
│
├── frontend/
│   └── dashboard.py
│
├── tests/
│
└── README.md
```

---

# ⚙️ Tech Stack

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Core programming language |
| FastAPI    | Backend API framework     |
| Streamlit  | Frontend dashboard        |
| Git/GitHub | Version control           |
| CSV Data   | Initial dataset storage   |

---

# ▶️ Running The Project

## 1. Clone Repository

```bash
git clone https://github.com/orashid90/clutch-player-analyser.git
```

---

## 2. Navigate Into Project

```bash
cd clutch-player-analyser
```

---

## 3. Install Dependencies

```bash
pip install fastapi uvicorn streamlit requests
```

---

# ▶️ Run Backend (FastAPI)

```bash
uvicorn app.main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

# ▶️ Run Frontend (Streamlit)

In a second terminal:

```bash
python -m streamlit run frontend/dashboard.py
```

Frontend runs on:

```text
http://localhost:8501
```

---

# 📡 Example API Endpoint

```text
http://127.0.0.1:8000/compare?player1=Palmer&player2=Saka
```

---

# 🧪 Example Output

```json
{
  "summary": "Palmer vs Saka - Clutch Dashboard",
  "winner": "Palmer",
  "insight": "Palmer has the stronger clutch rating based on weighted clutch impact and average moment quality."
}
```

---

# 🔮 Future Improvements

Planned upgrades include:

* opponent strength weighting
* assists support
* real football datasets/API integration
* database integration
* automated testing
* cloud deployment
* CI/CD pipelines
* authentication
* advanced visual analytics
* seasonal comparisons
* clutch trends over time

---

# 📚 Learning Goals

This project is also being used as a hands-on learning journey into:

* backend engineering
* API design
* software architecture
* frontend dashboards
* analytics engineering
* Git/GitHub workflows
* deployment pipelines
* product thinking

---

# 👤 Author

Built by Omar Rashid as a football analytics learning project.
