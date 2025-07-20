# personal daily reminder
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

if time_bound == "yes":
    note = "Time-sensitive task."

match priority:
    case "high":
        if time_bound == "yes":
            print("Reminder: 'Finish project report' is a high priority task with a deadline.")
        else:
            print("Reminder: 'Finish project report' is a high priority task.")
    case "medium":
        print("Reminder: 'Finish project report soon'")
    case "low":
        if time_bound == "no":
            print("Note: 'Read a book' is a low priority task. Consider completing it when free.")
        else:
            print("Note: Low priority task added.")
    case _:
        print("Invalid input")
