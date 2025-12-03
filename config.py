from dotenv import load_dotenv
import os

# Load .env file in the same folder as config.py
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

# Celcom SMS API credentials
CELCOM_API_URL = os.getenv("CELCOM_API_URL")
CELCOM_API_KEY = os.getenv("CELCOM_API_KEY")
CELCOM_PARTNER_ID = os.getenv("CELCOM_PARTNER_ID")
CELCOM_SHORTCODE = os.getenv("CELCOM_SHORTCODE")
CELCOM_USER_ID = os.getenv("CELCOM_USER_ID")
CELCOM_PASSWORD = os.getenv("CELCOM_PASSWORD")

# Flask secret key
SECRET_KEY = os.getenv("SECRET_KEY")

# Admin REST PIN
ADMIN_PIN = os.getenv("ADMIN_PIN")

# Email credentials
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

# Admin login credentials
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")

# Ensure instance folder exists
if not os.path.exists(INSTANCE_DIR):
    os.makedirs(INSTANCE_DIR)

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(INSTANCE_DIR, "contacts.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False

