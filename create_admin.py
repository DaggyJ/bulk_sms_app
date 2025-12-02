# create_admin.py
from app import app
from models import db, User
from werkzeug.security import generate_password_hash
from config import (
    ADMIN_USERNAME,
    ADMIN_PASSWORD,
    ADMIN_PIN,
    EMAIL_USER,
    EMAIL_PASS,
    SECRET_KEY,
    CELCOM_PARTNER_ID,
    CELCOM_API_KEY
)

with app.app_context():
    # Check if admin already exists
    existing_admin = User.query.filter_by(username=ADMIN_USERNAME).first()
    if existing_admin:
        print(f"Admin user '{ADMIN_USERNAME}' already exists.")
    else:
        # Create the admin user
        admin = User(
            username=ADMIN_USERNAME,
            password_hash=generate_password_hash(ADMIN_PASSWORD),
            is_admin=True,
            rest_pin=ADMIN_PIN
        )
        db.session.add(admin)
        db.session.commit()
        print(f"Admin user '{ADMIN_USERNAME}' created successfully!")

    # Optional: Print loaded configs to confirm
    print("\nLoaded Configs:")
    print("SECRET_KEY:", SECRET_KEY)
    print("EMAIL_USER:", EMAIL_USER)
    print("EMAIL_PASS:", EMAIL_PASS)
    print("CELCOM_PARTNER_ID:", CELCOM_PARTNER_ID)
    print("CELCOM_API_KEY:", CELCOM_API_KEY)
