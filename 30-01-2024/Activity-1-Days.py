def convert_to_days():
   hours = int(input("Insert Hours:"))
   minutes = int(input("Insert Minutes:"))
   seconds = int(input("Insert Seconds:"))
   days = get_days(hours, minutes, seconds)
   print(f"It is {round(float(days), 4)} days☀️") 
  
def get_days(hours, minutes, seconds):
   days = (hours/24) + (minutes/1440) + (seconds/86400)
   return days
  
convert_to_days()
   