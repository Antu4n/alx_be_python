#datetime module
from datetime import datetime
from datetime import timedelta
def display_current_datetime():
	current_date = datetime.now()
	current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
	print(f"Current date and time: {current_date}")
display_current_datetime()

days = int(input("Enter number of days to add to the current date: "))
def calculate_future_date(days):
	current_date = datetime.now()
	future_date = (current_date + timedelta(days = days))
	future_date = future_date.strftime("%Y-%m-%d")
	print(f"Future date: {future_date}")

calculate_future_date(days)
