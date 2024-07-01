# Prompt User Input with 'task' variable
task_reminder = input("Enter your task: ")

# Prompt User Input with 'priority' variable
priority = input("Priority (high/medium/low): ").lower()

# Prompt User Input with 'urgency' variable
urgency = input("Is it time-bound? (yes/no): ").lower()

# Customised Reminder with 'f' format
reminder = f"'{task_reminder}' is a {priority} priority task"

# Use 'match case' condition to evaluate 'priority' variable
match priority:
    case "high":
        if urgency == "yes":
            time_bound = ""
            reminder += time_bound if time_bound else " that requires immediate attention today!."
            print(f"\nReminder: {reminder}")
    case "medium":
        if urgency == "no":
            time_bound = ""
            reminder += time_bound if time_bound else ". Consider completing it when you have free time."
            print(f"\nReminder: {reminder}")
    case "low":
        if urgency == "no":
            time_bound = ""
            reminder += time_bound if time_bound else ". Consider completing it when you have free time."
            print(f"\nNote: {reminder}")

