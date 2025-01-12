FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

def convert_to_celsius(fahrenheit):
  #°C = (°F - 32) ÷ (9/5)
 
  C=(fahrenheit*FAHRENHEIT_TO_CELSIUS_FACTOR)+32
  return C

def convert_to_fahrenheit(celsius):
    F=(celsius-32)/CELSIUS_TO_FAHRENHEIT_FACTOR
    return F

temp=int(input("Enter the temperature to convert: "))
choice=input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
C1=convert_to_celsius(temp)

if choice=="F":
  F1=convert_to_fahrenheit(temp)
  print(temp,"°C is",F1,"°F")
elif choice=="C":
  C1=convert_to_celsius(temp)
  print(temp,"°F is",C1,"°C")
else:
  print("Invalid temperature. Please enter a numeric value.")  
