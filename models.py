from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    rest_pin = db.Column(db.String(6))
    status = db.Column(db.String(20), default="pending")  # pending, approved, disabled

    def is_active(self):
        return self.status == "approved"

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    region = db.Column(db.String(50))
    subregion = db.Column(db.String(50))

class SMSLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    recipients = db.Column(db.Text)
    category = db.Column(db.String(100))
    sent_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    api_response = db.Column(db.Text)  # ADD THIS FIELD


    
    
    
