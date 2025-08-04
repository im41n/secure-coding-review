# This script has multiple security flaws!!!!!!!!

import sqlite3

def login():
    username = input("Enter your username: ")  # No input validation (any input is accepted)
    password = input("Enter your password: ")  # Password not hidden / not hashed

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # SQL injection risk: user input is directly added to SQL string
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        print("Login successful!")  # Vague message (no details)
    else:
        print("Invalid credentials")

    conn.close()

login()
