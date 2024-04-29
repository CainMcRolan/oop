def printer():
   for i in range(1, 101):
      if i % 3 == 0 and i % 5 == 0:
         print("OOP")
      elif i % 3 == 0:
         print("Object Oriented")
      elif i % 5 ==0:
         print("Programming")
      else: 
         print(i)
printer()