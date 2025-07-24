#temp conversion
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
	celsius = ((fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR)
	print(f"{fahrenheit}°F is {round(celsius, 1)}°C")
def convert_to_fahrenheit(celsius):
	fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR)+32
	print(f"{celsius}°C is {round(fahrenheit,1)}°F")

while True:
	temperature = float(input("Enter the temperature to convert: "))
	if isinstance(temperature, float) == False:
		float(input("Please enter a numeric value: "))
		continue
	degree = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
	if degree == "c":
		convert_to_fahrenheit(temperature)
	elif degree == "f":
		convert_to_celsius(temperature)
	else: 
		print("Enter Valid input") 
		continue

	break
