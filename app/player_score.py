import csv
from app.scoring import clutch_score


def calculate_player_total(player_name):
    total = 0

    with open("data/events.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["player"].lower() == player_name.lower():
                total += clutch_score(
                    int(row["goal_difference_before_goal"]),
                    int(row["minute"]),
                )

    return total


def leaderboard():
    import csv

    scores = {}

    with open("data/events.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            player = row["player"]

            event_score = clutch_score(
                int(row["goal_difference_before_goal"]),
                int(row["minute"])
            )

            if player not in scores:
                scores[player] = 0

            scores[player] += event_score


    items = scores.items()
    sorted_items = sorted(items, key=lambda item: item[1], reverse=True)
    leaderboard = dict(sorted_items)

    return leaderboard


def player_events(player_name):
    import csv

    events = []
    total_score = 0

    with open("data/events.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["player"].lower() == player_name.lower():
                score = clutch_score(
                    int(row["goal_difference_before_goal"]),
                    int(row["minute"])
                )

                event = {
                    "minute": int(row["minute"]),
                    "goal_difference_before_goal": int(row["goal_difference_before_goal"]),
                    "clutch_score": score
                }

                events.append(event)
                total_score += score

    sorted_events = sorted(
        events,
        key=lambda event: event["clutch_score"],
        reverse=True
    )

    best_moment = sorted_events[0] if sorted_events else None

    return {
        "player": player_name,
        "total_events": len(events),
        "total_clutch_score": total_score,
        "average_clutch_score": round(total_score / len(events), 2) if events else 0,
        "best_moment": best_moment,
        "events": sorted_events
    }


def player_clutch_profile(player_name):
    player_data = player_events(player_name)

    events = player_data["events"]

    if not events:
        return {
            "player": player_name,
            "comfort_vs_clutch_ratio": 0,
            "label": "No Data",
            "description": "No events available for this player"
        }

    comfort_events = 0
    neutral_events = 0
    clutch_events = 0

    for event in events:
        score = event["clutch_score"]
        
        if score <= 3:
            comfort_events += 1
        elif score <= 7:
            neutral_events += 1
        else:
            clutch_events += 1

    total_events = len(events)
    comfort_ratio = round((comfort_events / total_events) * 100, 2)

    if comfort_events > neutral_events and comfort_events > clutch_events:
        label = "Comfort Merchant"
        description = "Majority of goals in low-pressure situations"
    elif clutch_events > comfort_events and clutch_events > neutral_events:
        label = "Clutch Player"
        description = "Majority of goals are scored in high-pressure moments i.e. when it matters"
    else:
        label = "Balanced"
        description = "Mix of clutch and low-pressure goals"

    return {
        "player": player_name,
        "comfort_ratio": comfort_ratio,
        "comfort_events": comfort_events,
        "clutch_events": clutch_events,
        "total_events": total_events,
        "label": label,
        "description": description
    }


def compare_players(player1, player2):

    player1_total = calculate_player_total(player1)
    player2_total = calculate_player_total(player2)

    player1_profile = player_clutch_profile(player1)
    player2_profile = player_clutch_profile(player2)

    player1_events = player_events(player1)
    player2_events = player_events(player2)

    return {
        "player1": {
            "name": player1,
            "total_clutch_score": player1_total,
            "average_clutch_score": player1_events["average_clutch_score"],
            "best_moment": player1_events["best_moment"],
            "clutch_profile": player1_profile
        },
        "player2": {
            "name": player2,
            "total_clutch_score": player2_total,
            "average_clutch_score": player2_events["average_clutch_score"],
            "best_moment": player2_events["best_moment"],
            "clutch_profile": player2_profile
        }
    }