#personal daily reminder
task = input("Enter task description: ")
priority = input("Enter task priority (high, medium, low): ")
time_bound = input("Is the task time_bound? (yes/no) ")

match priority:
	case "high" if (time_bound == "yes"):
		print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
	case "high" if (time_bound == "no"):
		print("Reminder: 'Finish project report' is a high priority task ")
	case "medium":
		print("Reminder: 'Finish project report soon'")
	case "low"  if (time_bound =="no"):
		print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
	case _:
		print("Invalid input")
