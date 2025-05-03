from flask import Blueprint, request, jsonify
from datetime import datetime
import random

fare_bp = Blueprint("fare", __name__)

@fare_bp.route("/fare", methods=["POST"])
def calculate_fare():
    data = request.get_json()

    pickup = data.get("pickupLocation")
    destination = data.get("destination")

    if not pickup or not destination:
        return jsonify({"error": "Missing pickup or destination"}), 400

    # Мокаем расстояние и ETA
    distance_km = round(random.uniform(3, 15), 1)  # допустим, 3–15 км
    rate_per_km_kzt = 300  # условный тариф, 300 тенге/км
    fare_estimate = round(distance_km * rate_per_km_kzt, 2)
    eta_minutes = random.randint(5, 15)

    return jsonify({
        "pickup": pickup,
        "destination": destination,
        "distance_km": distance_km,
        "fare": fare_estimate,
        "eta_minutes": eta_minutes,
        "currency": "KZT",
        "timestamp": datetime.utcnow().isoformat()
    }), 200
