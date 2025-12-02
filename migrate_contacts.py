import sqlite3
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, "instance", "contacts.db")

conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Check existing columns
cur.execute("PRAGMA table_info(contact);")
columns = [col[1] for col in cur.fetchall()]
print("Existing columns:", columns)

# Add category column if it does not exist
if "category" not in columns:
    cur.execute("ALTER TABLE contact ADD COLUMN category TEXT")
    print("Added 'category' column to contact table")
else:
    print("'category' column already exists")

conn.commit()
conn.close()
