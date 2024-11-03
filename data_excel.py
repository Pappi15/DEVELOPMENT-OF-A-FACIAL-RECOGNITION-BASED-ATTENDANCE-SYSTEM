import sqlite3 as sl
import pandas as pd
from datetime import datetime

# Connect to the SQLite database
con = sl.connect('data.db')

# Query the USER table
with con:
    data = con.execute("SELECT id, name, time FROM USER")
    rows = data.fetchall()

# Process the data
attendance_data = {}
for row in rows:
    student_id = row[0]
    name = row[1]
    time_str = row[2]

    # Convert the datetime string to a datetime object
    try:
        dt = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
        week = dt.strftime('%Y-%U')  # Year and Week number
    except ValueError:
        print(f"Error: {time_str} is not a valid datetime format.")
        continue

    if student_id not in attendance_data:
        attendance_data[student_id] = {'name': name, 'weeks': set()}
    attendance_data[student_id]['weeks'].add(week)

# Prepare the data for the DataFrame
processed_data = []
for student_id, info in attendance_data.items():
    processed_data.append({
        'Matric Number': student_id,
        'Name': info['name'],
        'Weeks Attended': len(info['weeks'])
    })

# Create a DataFrame
df = pd.DataFrame(processed_data)

# Write the DataFrame to an Excel file
df.to_excel('student_attendance.xlsx', index=False)

print("Data has been written to student_attendance.xlsx")
