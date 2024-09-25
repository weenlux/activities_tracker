from flask import Flask, request, jsonify, send_file
import csv
import sqlite3
import os

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('activities.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS activities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            activity TEXT,
            duration REAL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Route to save activity data to the database
@app.route("/save-activity", methods=["POST"])
def save_activity():
    data = request.json
    conn = sqlite3.connect('activities.db')
    c = conn.cursor()
    
    # Insert the activity data into the database
    c.execute('INSERT INTO activities (date, activity, duration) VALUES (?, ?, ?)', 
              (data['date'], data['activity'], data['duration']))
    
    conn.commit()
    conn.close()
    
    return jsonify({"status": "success"}), 200

# API to retrieve all activities
@app.route("/get-activities", methods=["GET"])
def get_activities():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM activities')
    rows = c.fetchall()
    conn.close()

    activities = []
    for row in rows:
        activities.append({
            "id": row[0],
            "date": row[1],
            "activity": row[2],
            "duration": row[3]
        })

    return jsonify(activities)
# Route to export data as CSV
@app.route("/export-csv")
def export_csv():
    conn = sqlite3.connect('activities.db')
    c = conn.cursor()
    c.execute('SELECT * FROM activities')
    rows = c.fetchall()
    conn.close()

    # Write to CSV
    csv_file = 'activities.csv'
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Date', 'Activity', 'Duration'])
        writer.writerows(rows)

    return send_file(csv_file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)