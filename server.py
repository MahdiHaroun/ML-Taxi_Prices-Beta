from flask import Flask, request, jsonify
from joblib import load
import numpy as np
from sklearn.preprocessing import StandardScaler
# Load the trained model
model = load("model.pkl")

# Load the scaler
scaler = load("scaler2.pkl")

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    trip_distance = data["trip_distance"]
    time_of_day = data["time_of_day"]
    day_of_week = data["day_of_week"]
    passenger_count = data["passenger_count"]
    traffic_conditions = data["traffic_conditions"]
    weather = data["weather"]
    trip_duration = data["trip_duration"]

    # Prepare the data for scaling
    Scaled_Data = [[trip_distance, time_of_day, day_of_week, passenger_count, traffic_conditions, weather, trip_duration]]
    standardScalar = StandardScaler()
    # Add debugging statements
    print("Scaled_Data before transformation:", Scaled_Data)
    
    # Transform the input data using the loaded scaler
    user_input_scaled = scaler.transform(Scaled_Data)
    # user_input_scaled2 = standardScalar.transform(user_input_scaled)
    # Add debugging statements
    print("user_input_scaled after transformation:", user_input_scaled)
    #print("user_input_scaled after transformation2:", user_input_scaled2)
    
    # Make a prediction
    prediction = model.predict(user_input_scaled)
    return jsonify({"fare": prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)