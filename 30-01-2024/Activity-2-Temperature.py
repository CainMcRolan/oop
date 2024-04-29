def convert_temp():
   temperature = float(input("Input Temperature in °F:"))
   celcius = convert_to_celcius(temperature)
   kelvin = convert_to_kelvin(celcius)
   print(f"{temperature}°F is {celcius}°C and {kelvin} K")
   
def convert_to_celcius(fahrenheit):
   celcius = (5/9) * (fahrenheit - 32)
   return celcius

def convert_to_kelvin(celcius):
   kelvin = celcius + 273.15
   return kelvin

convert_temp()