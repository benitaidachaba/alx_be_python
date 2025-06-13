from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"📅 Current date and time: {formatted_date}")
    return current_date  # In case we need it later

def calculate_future_date():
    try:
        days_to_add = int(input("📥 Enter the number of days to add to the current date: ").strip())
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"📆 Future date: {formatted_future_date}")
    except ValueError:
        print("❌ Invalid input. Please enter a valid number of days (integer).")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
# This code demonstrates how to work with dates and times in Python using the datetime module.
# It displays the current date and time, and allows the user to calculate a future date by adding a specified number of days.