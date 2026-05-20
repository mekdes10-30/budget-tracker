# Student Budget Tracker

A simple web app to help university students manage their money.

## About

I built this project to practice Python and Flask while solving a real problem — 
keeping track of income and expenses as a university student. 
It uses SQLite to store transactions and displays everything in a clean dashboard.

## Features

- Add income and expense transactions
- View your current balance
- Categorize spending (Food, Transport, Books, etc.)
- View full transaction history
- Delete transactions

## Built With

- Python
- Flask
- SQLite
- HTML and CSS

## How To Run

1. Clone the repository
   git clone https://github.com/mekdes10-30/budget-tracker.git

2. Navigate to the project folder
   cd budget-tracker

3. Create and activate virtual environment
   python -m venv venv
   venv\Scripts\activate

4. Install dependencies
   pip install flask

5. Run the app
   python app.py

6. Open your browser and go to http://127.0.0.1:5000

## Project Structure

- app.py — Flask routes and app logic
- database.py — Database setup and SQL queries
- templates/ — HTML pages (base, dashboard, add transaction)
