# Secure version with fixes applied!!!!!!!!!!!!!!!
import sqlite3         # Connects to the database
import getpass         # Hides password input in terminal
import hashlib         # Hashes the password for security
def hash_password(password):        # Function to hash password
    return hashlib.sha256(password.encode()).hexdigest()
def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")  # Hidden password input
    hashed_pw = hash_password(password)          # Convert password to hashed form

    conn = sqlite3.connect("users.db")   # Connect to database file
    cursor = conn.cursor()              # Used to run database commands

    # Prevent SQL injection with parameterized query
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, hashed_pw))
    result = cursor.fetchone()
    if result:
        print("Login successful!")
    else:
        print("Login failed. Check your credentials.")

    conn.close()
login()
