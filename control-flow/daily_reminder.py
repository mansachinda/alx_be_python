# Prompt User Input with 'task' variable
task = input("Enter your task: ")
# Prompt User Input with 'priority' variable
priority = input("Priority (high/medium/low): ")
# Prompt User Input with 'time_bound' variable
time_bound = str(input("Is it time-bound? (yes/no): "))

# Use 'match case' condition to evaluate 'priority' variable 
match task:
    case priority:
        # Use 'if', 'elif' condition to evaluate 'time_bound' variable
        if time_bound == 'yes':
            print("\nReminder:", task, "is a high priority task that requires immediate attention today!")
        elif time_bound == 'no':
            print("\nNote:", task, "is a low priority task. Consider completing it when you have free time.")

