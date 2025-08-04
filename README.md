# CodeAlpha – Secure Coding Review (Task 3)

This project was created as part of my cybersecurity internship with **CodeAlpha**. The goal was to analyze and fix a vulnerable piece of code by applying secure coding practices.

## Objective

The original script was a basic login system written in Python, but it contained several serious security flaws:
- SQL Injection vulnerability  
- Plaintext password storage  
- No input validation  
- Vague error messages

## Fixes Applied

- Replaced string-based SQL queries with **parameterized queries**
- Added **password hashing** using SHA-256
- Used `getpass` to **hide password input**
- Wrote clear, user-friendly login messages
