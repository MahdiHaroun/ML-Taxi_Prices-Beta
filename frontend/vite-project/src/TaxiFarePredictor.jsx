import React, { useState } from "react";
import axios from "axios";

const TaxiFarePredictor = () => {
  const [formData, setFormData] = useState({
    tripDistance: "",
    timeOfDay: "",
    dayOfWeek: "",
    passengerCount: "",
    trafficConditions: "",
    weather: "",
    tripDuration: "",
  });

  const [fare, setFare] = useState(null);

  // Mappings for dropdown values
  const timeOfDayMap = { Morning: 0, Afternoon: 1, Evening: 2, Night: 3 };
  const dayOfWeekMap = { Weekday: 0, Weekend: 1 };
  const trafficConditionsMap = { Low: 0, Medium: 1, High: 2 };
  const weatherMap = { Clear: 0, Rain: 1, Snow: 2 };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Convert user-friendly inputs to API-friendly format
      const requestData = {
        trip_distance: parseFloat(formData.tripDistance),
        time_of_day: timeOfDayMap[formData.timeOfDay],
        day_of_week: dayOfWeekMap[formData.dayOfWeek],
        passenger_count: parseInt(formData.passengerCount),
        traffic_conditions: trafficConditionsMap[formData.trafficConditions],
        weather: weatherMap[formData.weather],
        trip_duration: parseFloat(formData.tripDuration),
      };

      // Make the API request
      const response = await axios.post(
        "http://127.0.0.1:5000/predict",
        requestData
      );

      // Set the predicted fare
      setFare(response.data.fare);
    } catch (error) {
      console.error("Error fetching fare:", error);
      setFare("An error occurred while calculating the fare.");
    }
  };

  return (
    <div style={{ padding: "20px", maxWidth: "500px", margin: "auto" }}>
      <h1>Taxi Fare Predictor</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Trip Distance (km):</label>
          <input
            type="number"
            step="0.01"
            name="tripDistance"
            value={formData.tripDistance}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Time of Day:</label>
          <select name="timeOfDay" value={formData.timeOfDay} onChange={handleChange} required>
            <option value="">Select...</option>
            <option value="Morning">Morning</option>
            <option value="Afternoon">Afternoon</option>
            <option value="Evening">Evening</option>
            <option value="Night">Night</option>
          </select>
        </div>
        <div>
          <label>Day of Week:</label>
          <select name="dayOfWeek" value={formData.dayOfWeek} onChange={handleChange} required>
            <option value="">Select...</option>
            <option value="Weekday">Weekday</option>
            <option value="Weekend">Weekend</option>
          </select>
        </div>
        <div>
          <label>Passenger Count:</label>
          <input
            type="number"
            name="passengerCount"
            min="1"
            max="4"
            value={formData.passengerCount}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Traffic Conditions:</label>
          <select
            name="trafficConditions"
            value={formData.trafficConditions}
            onChange={handleChange}
            required
          >
            <option value="">Select...</option>
            <option value="Low">Low</option>
            <option value="Medium">Medium</option>
            <option value="High">High</option>
          </select>
        </div>
        <div>
          <label>Weather:</label>
          <select name="weather" value={formData.weather} onChange={handleChange} required>
            <option value="">Select...</option>
            <option value="Clear">Clear</option>
            <option value="Rain">Rain</option>
            <option value="Snow">Snow</option>
          </select>
        </div>
        <div>
          <label>Trip Duration (minutes):</label>
          <input
            type="number"
            step="0.01"
            name="tripDuration"
            value={formData.tripDuration}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit" style={{ marginTop: "10px" }}>
          Predict Fare
        </button>
      </form>
      {fare !== null && (
        <div style={{ marginTop: "20px", fontWeight: "bold" }}>
          Predicted Fare: {fare}
        </div>
      )}
    </div>
  );
};

export default TaxiFarePredictor;
