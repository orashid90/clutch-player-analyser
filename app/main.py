from fastapi import FastAPI
from app.player_score import calculate_player_total, leaderboard, player_events, comfort_clutch_ratio

app = FastAPI()


@app.get("/player/{player_name}")
def get_player_score(player_name: str):
    total_score = calculate_player_total(player_name)

    return {
        "player": player_name,
        "clutch_score": total_score
    }


@app.get("/leaderboard")
def get_leaderboard():
    return leaderboard()


@app.get("/player/{player_name}/events")
def get_player_events(player_name: str):
    return player_events(player_name)


@app.get("/player/{player_name}/comfort_clutch")
def get_comfort_clutch_ratio(player_name: str):
    return comfort_clutch_ratio(player_name) 
    





  # $ python -m uvicorn app.main:app --reload