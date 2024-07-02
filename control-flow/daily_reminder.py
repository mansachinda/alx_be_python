# Prompt User Input with 'task' variable
task_reminder = input("Enter your task: ")

# Prompt User Input with 'priority' variable
task_priority = input("Priority (high/medium/low): ").lower()

# Prompt User Input with 'urgency' variable
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Customised Reminder with 'f' format
reminder = f"'{task_reminder}' is a {task_priority} priority task"

# 'Match Case' condition to evaluate 'task_priority' variable
match task_priority:
    case "high":
        print(f"\nReminder: {reminder}", end="")
    case "medium":
        print(f"\nReminder: {reminder}", end="")
    case "low":
        print(f"\nNote: {reminder}", end="")

# 'If', "Else' condition to evaluate 'time_bound' variable
if time_bound == "yes":
    print(" that requires immediate attention today!")
else:
    print(". Consider completing it when you have free time.")

