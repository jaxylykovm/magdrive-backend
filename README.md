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
- **Random (for mocked fare + ETA)**

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/jaxylykovm/magdrive-backend.git
cd magdrive-backend
2. Create a Virtual Environment
bash
Копировать
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
bash
Копировать
pip install -r requirements.txt
4. Setup PostgreSQL
Make sure you have a PostgreSQL server running and a database named magdrive created:

bash
Копировать
psql -U <your-username>
CREATE DATABASE magdrive;
Update the connection string in config.py if necessary.

5. Run the Server
bash
Копировать
python main.py
The server will start at http://localhost:5000

📬 API Endpoints
1. Estimate Fare
POST /fare

Request Body
json
Копировать
{
  "pickupLocation": "Almaty",
  "destination": "Kaskelen"
}
Response
json
Копировать
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

Request Body
json
Копировать
{
  "pickupLocation": "Almaty",
  "destination": "Kaskelen"
}
Response
json
Копировать
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

Response
json
Копировать
{
  "ride_id": "uuid",
  "status": "completed"
}
📁 Folder Structure
arduino
Копировать
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
│
├── main.py
├── requirements.txt
└── README.md
