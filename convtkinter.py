import tkinter as tk
window = tk.Tk()
window.title("Temperature Converter")
window.geometry("300x150")
window.resizable(False, False)
def convert():
  tempunit = temp.get()
  temp_val = tempVal.get()
  temp_unit = tempconv.get()
  if tempunit.lower() == "celsius" and temp_unit.lower() == "kelvin":
    newtemp = int(temp_val) + 273.15
    temp_str = str(newtemp)    
    result.set("Converting " + temp_val + " degree " + tempunit + " to kelvin will give " + temp_str  + " degree kelvin")
  elif tempunit.lower() == "celsius" and temp_unit.lower() == "fahrenheit":
    newtemp = ((1.8) * int(temp_val)) + 32
    temp_str = str(newtemp)
    result.set("Converting " + temp_val + " degree " + tempunit + " to fahrenheit will give " + temp_str + " degree fahrenheit")
  elif tempunit.lower() == "kelvin"  and temp_unit.lower() == "celsius":
    newtemp = float(temp_val) - 273.15
    temp_str = str(newtemp)
    result.set("Converting " + temp_val + " degree " + tempunit + " to celsius will give " + temp_str + " degree celsius")
  elif tempunit.lower() == "kelvin" and temp_unit.lower() == "fahrenheit":
    newtemp = (1.8*(int(temp_val)-273.15))+32
    temp_str = str(newtemp)
    result.set("Converting " + temp_val + " degree " + tempunit + " to fahrenheit will give " + temp_str + " degree fahrenheit")
  elif tempunit.lower() == "fahrenheit" and temp_unit.lower() == "celsius":
    newtemp = ((int(temp_val) - 32)*0.5556) 
    temp_str = str(newtemp)
    result.set("Converting " + temp_val + " degree " + tempunit + " to celsius will give " + temp_str + " degree celsius")
  elif tempunit.lower() == "fahrenheit" and temp_unit.lower() == "kelvin":
    newtemp = ((int(temp_val) - 32)*0.5556)+273.15
    temp_str = str(newtemp)
    result.set("Converting " + temp_val + " degree " + tempunit + " to kelvin will give " + temp_str + " degree kelvin")

tempLabel = tk.Label(text = "Type in Temperature unit you're converting from")
tempLabel.pack()  
temp = tk.StringVar()
tempEntry = tk.Entry(textvariable = temp)
tempEntry.pack()
tempValLabel = tk.Label(text = "Type in Temperature value")
tempValLabel.pack()  
tempVal = tk.StringVar()
tempValEntry = tk.Entry(textvariable = tempVal)
tempValEntry.pack()
tempconvLabel = tk.Label(text = "Type in Temperature unit you're converting to")
tempconvLabel.pack()  
tempconv = tk.StringVar()
tempconvEntry = tk.Entry(textvariable = tempconv)
tempconvEntry.pack()
button = tk.Button(text = "Convert", command=convert)
button.pack()
result = tk.StringVar()
resultLabel = tk.Label(textvariable = result)
resultLabel.pack()
window.mainloop()