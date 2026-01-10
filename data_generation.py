import random
import pandas as pd

def generate_elevator_data(num_samples=100):
    data = []

    for t in range(num_samples):
        sample = {
            "time": t,
            "load_kg": random.randint(100, 800),
            "vibration": round(random.uniform(0.1, 2.5), 2),
            "motor_temp": random.randint(40, 95),
            "door_time": round(random.uniform(1.5, 5.0), 2),
            "trips_last_hour": random.randint(1, 25)
        }
        data.append(sample)

    return pd.DataFrame(data)


if __name__ == "__main__":
    df = generate_elevator_data()
    df.to_csv("synthetic_elevator_data.csv", index=False)
    print("Synthetic elevator data generated.")
