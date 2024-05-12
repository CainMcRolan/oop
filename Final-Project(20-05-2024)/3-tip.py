def main():
   try:
      dollars = dollars_to_float(input("How much was the meal? "))
   except ValueError:
      print("Invalid Input")
      return

   try:
      percent = percent_to_float(input("What percentage would you like to tip? "))
   except ValueError:
      print("Invalid Input")
      return
   
   tip = dollars * percent
   print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
   dollars = d.replace('$', '')
   return float(dollars)

def percent_to_float(p):
   percent = p.replace('%', '')
   return float(percent) / 100.0

main()