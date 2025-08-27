import json
import os
import dateparser
from dateparser.search import search_dates
from apscheduler.schedulers.background import BackgroundScheduler

REMINDER_FILE = "data/reminders.json"
scheduler = BackgroundScheduler()
scheduler.start()

# Ensure data directory exists
if not os.path.exists("data"):
    os.makedirs("data")


def load_existing_reminders(speak):
    if os.path.exists(REMINDER_FILE):
        with open(REMINDER_FILE, "r") as f:
            reminders = json.load(f)

        for item in reminders:
            run_date = dateparser.parse(item["time"])
            if run_date:
                scheduler.add_job(lambda msg=item["text"]: speak(f"⏰ Reminder: {msg}"),
                                  'date', run_date=run_date)
        print(f"Loaded {len(reminders)} reminders.")
    else:
        with open(REMINDER_FILE, "w") as f:
            json.dump([], f)


def schedule_reminder(full_text, speak):
    # Extract datetime from text
    results = search_dates(full_text, settings={'PREFER_DATES_FROM': 'future'})

    if results:
        # Get first date and its span
        date_str, reminder_time = results[0]
        # Extract message by removing the date string
        reminder_msg = full_text.replace(date_str, "").strip()
        if not reminder_msg:
            reminder_msg = "This is your reminder."

        # Schedule the reminder
        scheduler.add_job(lambda: speak(f"⏰ Reminder: {reminder_msg}"),
                          'date', run_date=reminder_time)
        speak(f"✅ Okay, I’ll remind you to '{reminder_msg}' at {reminder_time.strftime('%I:%M %p')}.")

        # Save to file
        reminders = []
        if os.path.exists(REMINDER_FILE):
            with open(REMINDER_FILE, "r") as f:
                reminders = json.load(f)
        reminders.append({"text": reminder_msg, "time": str(reminder_time)})
        with open(REMINDER_FILE, "w") as f:
            json.dump(reminders, f, indent=4)
    else:
        speak("⚠️ Sorry, I couldn't understand the reminder message or time.")
