# personal daily reminder
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        print("Reminder: 'Finish project report' is a high priority task with a deadline.")
    case "high" if time_bound == "no":
        print("Reminder: 'Finish project report' is a high priority task.")
    case "medium":
        print("Reminder: 'Finish project report soon'")
    case "low" if time_bound == "no":
        print("Note: 'Read a book' is a low priority task. Consider completing it when free.")
    case _:
        print("Invalid input")
