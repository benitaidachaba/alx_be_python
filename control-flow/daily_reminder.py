task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")


match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Focus on '{task}' first. It's high priority even if not time-bound.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed by the end of the day.")
        else:
            print(f"Plan to do '{task}' after handling high priority tasks.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task but still requires attention today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Unknown priority entered.")
# This code takes a task, its priority, and whether it is time-bound or not, and provides reminders based on the priority level.