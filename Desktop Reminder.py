from plyer import notification
import time

def get_user_input():
    try:
        toast_title = input("\nEnter the Title of Reminder: ").strip()
        if not toast_title:
            raise ValueError("Title cannot be empty.")
        
        msg = input("\nEnter the Reminder: ").strip()
        if not msg:
            raise ValueError("Message cannot be empty.")
        
        minutes = float(input("\nHow Many Minutes: "))
        if minutes <= 0:
            raise ValueError("Minutes should be a positive number.")
        
        return toast_title, msg, minutes
    except ValueError as e:
        print(f"Input error: {e}")
        return None

def set_reminder(toast_title, msg, minutes):
    seconds = minutes * 60
    print("\nReminder Set Successfully")

    time.sleep(seconds)
    notification.notify(
        title=toast_title,
        message=msg,
        timeout=10
    )

def main():
    user_input = get_user_input()
    if user_input:
        toast_title, msg, minutes = user_input
        set_reminder(toast_title, msg, minutes)

if __name__ == "__main__":
    main()
