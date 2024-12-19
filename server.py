from flask import Flask, request, jsonify
from joblib import load

# Load the trained model
model = load("taxi_model.pkl")

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    time = data["time"]
    traffic = data["traffic"]
    distance = data["distance"]
    
    # Make a prediction
    prediction = model.predict([[time, traffic, distance]])
    return jsonify({"fare": prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)
