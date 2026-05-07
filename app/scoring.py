def game_state_score(goal_difference_before_goal):
    if goal_difference_before_goal <= -3:
        return 1
    elif goal_difference_before_goal >= 2:
        return 1
    elif goal_difference_before_goal == 1:
        return 2
    elif goal_difference_before_goal == -2:
        return 2
    elif goal_difference_before_goal == -1:
        return 3
    elif goal_difference_before_goal == 0:
        return 4

def minute_score(minute):
    if minute <= 45:
        return 1
    elif minute <= 75:
        return 2
    elif minute <= 90:
        return 3
    return 4

def clutch_score(goal_difference_before_goal, minute):
    return game_state_score(goal_difference_before_goal) * minute_score(minute)


