from flask import Flask, request, jsonify
from joblib import load
import numpy as np
from sklearn.preprocessing import StandardScaler
from flask_cors import CORS
# Load the trained model
model = load("model.pkl")

# Load the scaler
scaler = load("scaler2.pkl")
app = Flask(__name__)
# Apply CORS to allow all origins
CORS(app)
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

    
    Scaled_Data = [[trip_distance, time_of_day, day_of_week, passenger_count, traffic_conditions, weather, trip_duration]]
    standardScalar = StandardScaler()
    
    print("Scaled_Data before transformation:", Scaled_Data)
    
   
    user_input_scaled = scaler.transform(Scaled_Data)
    print("user_input_scaled after transformation:", user_input_scaled)
    
    
    
    prediction = model.predict(user_input_scaled)
    return jsonify({"Predicted_Trip_Price": prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)