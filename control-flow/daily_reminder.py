task = input("Enter your task: ")
priority = input("priority (high/medium/low): ")
time_bound = input("is it time-bound (yes/no): ")

while True:
    match priority:
        case "high":
            if time_bound.lower() == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print("Focus on this task first.")
        case "medium":
            if time_bound.lower() == "yes":
                print(f"Reminder: '{task}' is a medium priority task that should be completed by the end of the day.")
            else:
                print("Plan to do this task after high priority ones.")
        case "low":
            if time_bound.lower() == "no":
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
            else:
                print("Do this task if you have extra time.")
        case _:
            print("Unknown priority entered.")
    break