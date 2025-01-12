FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

def convert_to_celsius(fahrenheit):
   return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  

def convert_to_fahrenheit(celsius):
     return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
     

temp=int(input("Enter the temperature to convert: "))
choice=input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if choice=="C":
  F1=convert_to_fahrenheit(temp)
  print(temp,"°C is",F1,"°F")
elif choice=="F":
  C1=convert_to_celsius(temp)
  print(temp,"°F is",C1,"°C")
else:
  print("Invalid temperature. Please enter a numeric value.")  
