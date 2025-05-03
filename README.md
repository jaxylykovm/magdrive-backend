# MAGDRIVE – Ride Sharing System 

This repository contains a partial backend implementation of the MAGDRIVE ride-sharing service using Flask and PostgreSQL.


##  Tech Stack

- Python 3.12  
- Flask  
- Flask-SQLAlchemy  
- PostgreSQL  
- Flask-CORS  
- UUID  
- Random (for mocked fare and ETA)

---

## Setup & Run

1. Clone the repository:
   ```bash
   git clone https://github.com/jaxylykovm/magdrive-backend.git
   cd magdrive-backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up PostgreSQL:
   - Create a database named `magdrive`
   - Ensure access credentials match those in `app/config.py`

5. Run the server:
   ```bash
   python main.py
   ```
   The service will run at `http://127.0.0.1:5000`

---

## 📬 API Endpoints

### 1. Estimate Fare

```http
POST /fare
Content-Type: application/json

Body:
{
  "pickupLocation": "Almaty",
  "destination": "Kaskelen"
}

Response 200:
{
  "pickup": "Almaty",
  "destination": "Kaskelen",
  "fare": 4200.00,
  "eta_minutes": 9,
  "currency": "KZT",
  "timestamp": "2025-05-03T15:55:35.274493"
}
```

### 2. Create Ride

```http
POST /rides
Content-Type: application/json

Body:
{
  "pickupLocation": "Almaty",
  "destination": "Kaskelen"
}

Response 201:
{
  "ride_id": "0f47ad96-3b38-47db-9940-5bf038ccf82b",
  "pickup": "Almaty",
  "destination": "Kaskelen",
  "fare": 3900.00,
  "eta_minutes": 12,
  "currency": "KZT",
  "status": "requested"
}
```

### 3. Complete Ride

```http
PATCH /rides/<ride_id>/complete

Response 200:
{
  "ride_id": "0f47ad96-3b38-47db-9940-5bf038ccf82b",
  "status": "completed"
}
```

---

## 📁 Project Structure

```
magdrive-backend/
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
```

---


