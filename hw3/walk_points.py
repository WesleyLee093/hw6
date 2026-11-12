def walk_points(laps: int) -> int:
    daily_limit = 2
    points_per_lap = 1
    completion_bonus = 1
    bonus_threshold = daily_limit * points_per_lap
    counted_laps = min(laps, daily_limit)
    points = 0
    bonus = 0
    for _ in range(counted_laps):
        points += points_per_lap
        if points == bonus_threshold:
            bonus = completion_bonus
    return points + bonus
