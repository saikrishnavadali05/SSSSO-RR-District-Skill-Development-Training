#Here's a Python script :
# Screenshot 2025-07-18 183957

def convert_temperature():
# Prompt user for input
user_input = input("Enter temperature (e.g. 100 C or 212 F): ")

# Parse input
try:
    temp, unit = user_input.split()
    temp = float(temp)
except ValueError:
    print("Invalid input format. Please use 'value unit' (e.g. 100 C).")
    return

# Convert temperature
if unit.upper() == 'C':
    converted_temp = temp * 9/5 + 32
    print(f"{converted_temp:.1f} F")
elif unit.upper() == 'F':
    converted_temp = (temp - 32) * 5/9
    print(f"{converted_temp:.1f} C")
else:
    print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
if name == "main":
convert_temperature()

#To run this script, save it as temp_converter.py and execute it using python temp_converter.py.

#For possible extensions, here's an updated version that includes Kelvin scale, input validation, and a loop for multiple conversions:

def convert_temperature():
while True:
# Prompt user for input
user_input = input("Enter temperature (e.g. 100 C, 212 F, or 373 K), or 'q' to quit: ")

    if user_input.lower() == 'q':
        break

    # Parse input
    try:
        temp, unit = user_input.split()
        temp = float(temp)
    except ValueError:
        print("Invalid input format. Please use 'value unit' (e.g. 100 C).")
        continue

    # Convert temperature
    if unit.upper() == 'C':
        fahrenheit = temp * 9/5 + 32
        kelvin = temp + 273.15
        print(f"{temp:.1f}°C is equal to {fahrenheit:.1f}°F and {kelvin:.1f}K")
    elif unit.upper() == 'F':
        celsius = (temp - 32) * 5/9
        kelvin = (temp - 32) * 5/9 + 273.15
        print(f"{temp:.1f}°F is equal to {celsius:.1f}°C and {kelvin:.1f}K")
    elif unit.upper() == 'K':
        celsius = temp - 273.15
        fahrenheit = (temp - 273.15) * 9/5 + 32
        print(f"{temp:.1f}K is equal to {celsius:.1f}°C and {fahrenheit:.1f}°F")
    else:
        print("Invalid unit. Please use 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")
if name == "main":
convert_temperature()

#This version also includes a simple loop that allows the user to perform multiple conversions without having to restart the program. To quit, the user can enter 'q'.

#For a GUI version using Tkinter, here's a basic implementation:

import tkinter as tk

class TemperatureConverter:
def init(self):
self.window = tk.Tk()
self.window.title("Temperature Converter")

    self.input_label = tk.Label(self.window, text="Enter temperature:")
    self.input_label.pack()

    self.input_entry = tk.Entry(self.window)
    self.input_entry.pack()

    self.unit_label = tk.Label(self.window, text="Select unit:")
    self.unit_label.pack()

    self.unit_var = tk.StringVar()
    self.unit_var.set("C")

    self.celsius_radio = tk.Radiobutton(self.window, text="Celsius", variable=self.unit_var, value="C")
    self.celsius_radio.pack()

    self.fahrenheit_radio = tk.Radiobutton(self.window, text="Fahrenheit", variable=self.unit_var, value="F")
    self.fahrenheit_radio.pack()

    self.kelvin_radio = tk.Radiobutton(self.window, text="Kelvin", variable=self.unit_var, value="K")
    self.kelvin_radio.pack()

    self.convert_button = tk.Button(self.window, text="Convert", command=self.convert_temperature)
    self.convert_button.pack()

    self.output_label = tk.Label(self.window, text="")
    self.output_label.pack()

def convert_temperature(self):
    try:
        temp = float(self.input_entry.get())
    except ValueError:
        self.output_label['text'] = "Invalid input format. Please enter a number."
        return

    unit = self.unit_var.get()

    if unit == 'C':
        fahrenheit = temp * 9/5 + 32
        kelvin = temp + 273.15
        self