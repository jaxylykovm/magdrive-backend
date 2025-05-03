# MAGDRIVE – Ride Sharing System (Backend)

This project is a partial implementation (~30%) of a ride-sharing backend system built with Flask and PostgreSQL. It includes basic functionality such as fare estimation and ride management, following a microservice-inspired modular structure.

---

## 🔧 Tech Stack

- **Python 3.12**
- **Flask**
- **Flask-SQLAlchemy**
- **PostgreSQL**
- **Flask-CORS**
- **UUID**
- **Random module (for mocked fare + ETA)**

---

##  Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/magdrive-backend.git
   cd magdrive-backend

Create a virtual environment:

bash
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
pip install -r requirements.txt
Set up PostgreSQL:
Make sure a database named magdrive exists and user has access.

Run the server:

bash
python main.py

API Endpoints
1. Estimate Fare
POST /fare

Request Body:

json
{
  "pickupLocation": "Almaty",
  "destination": "Kaskelen"
}
Response:

json
{
  "pickup": "Almaty",
  "destination": "Kaskelen",
  "fare": 4200.00,
  "eta_minutes": 9,
  "currency": "KZT",
  "timestamp": "2025-05-03T15:55:35.274493"
}
2. Create Ride
POST /rides

Request Body:

json
{
  "pickupLocation": "Almaty",
  "destination": "Kaskelen"
}
Response:

json
{
  "ride_id": "uuid",
  "pickup": "Almaty",
  "destination": "Kaskelen",
  "fare": 3900.00,
  "eta_minutes": 12,
  "currency": "KZT",
  "status": "requested"
}
3. Complete Ride
PATCH /rides/<ride_id>/complete

Response:

json
{
  "ride_id": "uuid",
  "status": "completed"
}

📁 Folder Structure
arduino
magdrive-backend/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── db.py
│   ├── models.py
│   └── routes/
│       ├── fare.py
│       └── ride.py
├── main.py
├── requirements.txt
└── README.md