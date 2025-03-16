from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

# User Model (For Authentication & User Management)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f"<User {self.username}>"

# Allergen Detection Model (For Storing Image & Results)
class AllergenDetection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    image_path = db.Column(db.String(255), nullable=False)
    detected_allergen = db.Column(db.String(100), nullable=False)
    confidence_score = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    user = db.relationship('User', backref=db.backref('detections', lazy=True))

    def __repr__(self):
        return f"<Detection {self.detected_allergen} - {self.confidence_score}>"

# Function to initialize database
def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
