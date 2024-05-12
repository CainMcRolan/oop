menu = {
   "Baja Taco": 4.25,
   "Burrito": 7.50,
   "Bowl": 8.50,
   "Nachos": 11.00,
   "Quesadilla": 8.50,
   "Super Burrito": 8.50,
   "Super Quesadilla": 9.50,
   "Taco": 3.00,
   "Tortilla Salad": 8.00
}

total = 0

try:
   while True:
      food = input("Item: ").title()
      if food in menu:
         total += menu[food]
         print(f"Total: ${total:.2f}")
      else:
         continue
except EOFError:
   print(f"Grand Total: ${total:.2f}")