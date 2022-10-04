import tkinter as tk
window = tk.Tk()
window.title("Temperature Converter")
window.configure(background = "yellow")

tempUnitLabel = tk.Label(text = "Which Temperature unit are you converting from?", bg = "yellow")
tempUnitLabel.pack()  
tempUnit = (
  ("Kelvin","kelvin"),
  ("Celsius", "celsius"),
  ("Fahrenhiet","fahrenheit")
  )
var = tk.StringVar()
for t in tempUnit:
  tk.Radiobutton(window, variable = var, text = t[0], value = t[1], bg = "yellow").pack(anchor = tk.W)

def convert():
  tempunit = var.get()
  temp_val = tempVal.get()
  temp_unit = vari.get()
  if tempunit.lower() == "celsius" and temp_unit.lower() == "kelvin":
    newtemp = float(temp_val) + 273.15
    temp_str = str(newtemp)    
    result.set("Converting " + temp_val + " degree " + tempunit + " to kelvin will give " + temp_str  + " degree kelvin")
  elif tempunit.lower() == "celsius" and temp_unit.lower() == "fahrenheit":
    newtemp = ((1.8) * float(temp_val)) + 32
    temp_str = str(newtemp)
    result.set("Converting " + temp_val + " degree " + tempunit + " to fahrenheit will give " + temp_str + " degree fahrenheit")
  elif tempunit.lower() == "kelvin"  and temp_unit.lower() == "celsius":
    newtemp = float(temp_val) - 273.15
    temp_str = str(newtemp)
    result.set("Converting " + temp_val + " degree " + tempunit + " to celsius will give " + temp_str + " degree celsius")
  elif tempunit.lower() == "kelvin" and temp_unit.lower() == "fahrenheit":
    newtemp = (1.8*(float(temp_val)-273.15))+32
    temp_str = str(newtemp)
    result.set("Converting " + temp_val + " degree " + tempunit + " to fahrenheit will give " + temp_str + " degree fahrenheit")
  elif tempunit.lower() == "fahrenheit" and temp_unit.lower() == "celsius":
    newtemp = ((float(temp_val) - 32)*0.5556) 
    temp_str = str(newtemp)
    result.set("Converting " + temp_val + " degree " + tempunit + " to celsius will give " + temp_str + " degree celsius")
  elif tempunit.lower() == "fahrenheit" and temp_unit.lower() == "kelvin":
    newtemp = ((float(temp_val) - 32)*0.5556)+273.15
    temp_str = str(newtemp)
    result.set("Converting " + temp_val + " degree " + tempunit + " to kelvin will give " + temp_str + " degree kelvin")
  elif tempunit.lower() == "fahrenheit" and temp_unit.lower() == "fahrenheit":
    result.set("Converting fahrenheit to fahrenheit?\nAre you high??")
  elif tempunit.lower() == "kelvin" and temp_unit.lower() == "kelvin":
    result.set("Converting kelvin to kelvin?\nAre you high??")
  elif tempunit.lower() == "celsius" and temp_unit.lower() == "celsius":
    result.set("Converting celsuis to celsuis?\nAre you high??")


tempValLabel = tk.Label(text = "Type in Temperature value", bg = "yellow")
tempValLabel.pack()  
tempVal = tk.StringVar()
tempValEntry = tk.Entry(textvariable = tempVal)
tempValEntry.pack()
tempConvLabel = tk.Label(text = "Which Temperature unit are you converting to?", bg = "yellow")
tempConvLabel.pack()  
tempConv = (
  ("Kelvin","kelvin"),
  ("Celsius", "celsius"),
  ("Fahrenhiet","fahrenheit")
  )
vari = tk.StringVar()
for t in tempUnit:
  tk.Radiobutton(window, variable = vari, text = t[0], value = t[1], bg = "yellow").pack(anchor = tk.W)
button = tk.Button(text = "Convert", bg = "yellow", command=convert)
button.pack()
result = tk.StringVar()
resultLabel = tk.Label(textvariable = result, bg = "yellow")
resultLabel.pack()

destroy = tk.Button(text = "Exit", bg = "yellow", command = window.destroy)
destroy.pack()

window.mainloop()