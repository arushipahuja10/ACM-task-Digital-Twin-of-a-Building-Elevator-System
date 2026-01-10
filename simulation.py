import pandas as pd
from digitalTwin import infer_digital_twin_state

def level(value, low, high):
    if value < low:
        return "Low"
    elif value < high:
        return "Normal"
    else:
        return "High"

def run_simulation():
    df = pd.read_csv("synthetic_elevator_data.csv")

    print("\nElevator Digital Twin\n")

    for _ in range(10):
        sample = df.sample(1).iloc[0]
        state = infer_digital_twin_state(sample)

        vib_level = level(sample["vibration"], 1.0, 2.0)
        temp_level = level(sample["motor_temp"], 60, 80)

        print(f"[Time {int(sample['time'])}]")
        print(f" Load: {int(sample['load_kg'])} kg | Trips/hr: {int(sample['trips_last_hour'])}")
        print(f" Vibration: {vib_level} | Motor Temp: {temp_level}")
        print(f"--> Twin State: {state.upper()}")

        if state == "Degrading":
            print("-->  Insight: Prolonged stress detected -> Maintenance recommended\n")
        elif state == "Stressed":
            print("--> Insight: Heavy usage causing temporary stress\n")
        else:
            print("--> Insight: System operating normally\n")

if __name__ == "__main__":
    run_simulation()
