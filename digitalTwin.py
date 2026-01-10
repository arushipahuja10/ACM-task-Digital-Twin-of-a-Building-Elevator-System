def infer_digital_twin_state(sample):
    stress_score = 0

    if sample["load_kg"] > 500:
        stress_score += 2
    if sample["vibration"] > 1.5:
        stress_score += 2

    if sample["motor_temp"] > 70:
        stress_score += 2

    if sample["door_time"] > 3.5:
        stress_score += 1

    if sample["trips_last_hour"] > 15:
        stress_score += 1

    if stress_score <= 2:
        return "Normal"
    elif stress_score <= 4:
        return "Stressed"
    elif stress_score <= 6:
        return "Degrading"
    else:
        return "Critical"
