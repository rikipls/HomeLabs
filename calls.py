import homework_notification
import sqlite3_functions

rows = sqlite3_functions.fetch_alerts()

meet_links = {}
def create_meet_link():
    return "YOUR MEET LINK HERE"

# If your meet link isn't already in the dictionary, it adds it. Otherwise it calls it. Used when multiple people from the same class are being sent a notification.
for row in rows:
    alert_id, name, course, email, due_date, phone_number = row
    if course in meet_links:
        meet_link = meet_links[course]
    else:
        meet_link = create_meet_link()
        meet_links[course] = meet_link
    homework_notification.send_homework_notification(name, course, email, due_date, phone_number, meet_link)

