from flask import Blueprint, request, jsonify
from app.models import Ride
from app.db import db
from datetime import datetime
import uuid
import random

ride_bp = Blueprint("ride", __name__)

@ride_bp.route("/rides", methods=["POST"])
def create_ride():
    data = request.get_json()
    pickup = data.get("pickupLocation")
    destination = data.get("destination")

    if not pickup or not destination:
        return jsonify({"error": "Missing pickup or destination"}), 400

    distance_km = round(random.uniform(3, 15), 1)
    rate_per_km = 300
    fare = round(distance_km * rate_per_km, 2)
    eta = random.randint(5, 15)

    ride = Ride(
        id=uuid.uuid4(),
        pickup=pickup,
        destination=destination,
        fare=fare,
        eta_minutes=eta,
        currency="KZT",
        status="requested",
        created_at=datetime.utcnow()
    )

    db.session.add(ride)
    db.session.commit()

    return jsonify({
        "ride_id": ride.id,
        "pickup": ride.pickup,
        "destination": ride.destination,
        "fare": ride.fare,
        "eta_minutes": ride.eta_minutes,
        "currency": ride.currency,
        "status": ride.status
    }), 201

@ride_bp.route("/rides/<ride_id>/complete", methods=["PATCH"])
def complete_ride(ride_id):
    ride = Ride.query.get(ride_id)

    if not ride:
        return jsonify({"error": "Ride not found"}), 404

    ride.status = "completed"
    db.session.commit()

    return jsonify({
        "ride_id": ride.id,
        "status": ride.status
    }), 200

