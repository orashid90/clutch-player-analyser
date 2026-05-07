from fastapi import FastAPI
from app.player_score import calculate_player_total, leaderboard, player_events, player_clutch_profile, compare_players

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
def get_player_clutch_profile(player_name: str):
    return player_clutch_profile(player_name) 
    

@app.get("/compare")
def compare(player1: str, player2: str):
    return compare_players(player1, player2)



  # $ python -m uvicorn app.main:app --reload