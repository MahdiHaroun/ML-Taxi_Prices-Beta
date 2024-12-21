from flask import Flask, request, jsonify
from flask_cors import CORS
from joblib import load
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the trained model and scaler
model = load("model2.pkl")
scaler = load("scaler2.pkl")

app = Flask(__name__)

# Apply CORS to allow all origins
CORS(app)

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
    user_input_scaled = scaler.transform(Scaled_Data)
    
    # Make a prediction
    prediction = model.predict(user_input_scaled)
    return jsonify({"fare": prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)
