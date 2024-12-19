from flask import Flask, request, jsonify
from joblib import load

# Load the trained model
model = load("model.pkl")

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    Trip_Distance_km = data["Trip_Distance_km"]
    Time_of_Day = data["Time_of_Day"]
    Day_of_Week = data["Day_of_Week"]
    Passenger_Count = data["Passenger_Count"]
    Traffic_Conditions = data["Traffic_Conditions"]
    Weather = data["Weather"]
    Base_Fare = data["Base_Fare"]
    Per_Km_Rate = data["Per_Km_Rate"]
    Per_Minute_Rate = data["Per_Minute_Rate"]
    Trip_Duration_Minutes = data["Trip_Duration_Minutes"]

    # Make a prediction
    prediction = model.predict([[Trip_Distance_km, Time_of_Day, Day_of_Week, Passenger_Count, Traffic_Conditions, Weather, Base_Fare, Per_Km_Rate, Per_Minute_Rate, Trip_Duration_Minutes]])
    return jsonify({"fare": prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)
