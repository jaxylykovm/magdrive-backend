from app.db import create_app, db
from app import models
from flask_cors import CORS
from app.routes.fare import fare_bp
from app.routes.ride import ride_bp

app = create_app()
CORS(app)

#register routes
app.register_blueprint(fare_bp)
app.register_blueprint(ride_bp)

with app.app_context():
    db.create_all()
    print("✅ All tables created successfully.")

if __name__ == "__main__":
    app.run(port=5000, debug=True)

