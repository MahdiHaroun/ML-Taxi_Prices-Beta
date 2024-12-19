from flask import Flask, request, jsonify
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the pre-fitted scaler
scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

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
    input_data = [[trip_distance, time_of_day, day_of_week, passenger_count, traffic_conditions, weather, trip_duration]]

    # Scale the data
    scaled_data = scaler.transform(input_data)

    # Make a prediction
    prediction = model.predict(scaled_data)
    return jsonify({"fare": prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)