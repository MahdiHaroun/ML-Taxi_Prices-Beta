from flask import Flask, request, jsonify
from joblib import load
from sklearn.preprocessing import StandardScaler
# Load the trained model
model = load("model.pkl")
standardScalar = StandardScaler()
model = load("model.pkl")

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

    # Make a prediction
    Scaled_Data = [[trip_distance, time_of_day, day_of_week, passenger_count, traffic_conditions, weather, trip_duration]]
    user_input_scaled = standardScalar.transform(Scaled_Data)
    prediction = model.predict(user_input_scaled)
    return jsonify({"fare": prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)
