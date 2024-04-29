import random
target = 0;
while (target < 10):
   number = random.randint(1,10)
   number2 = random.randint(1,10)
   try:
      user_guess = int(input(f"{number} + {number2} = "))
      if (user_guess == number + number2):
         target += 1
         print(f"Correct \nscore: {target}")
      else:
         target -= 1
         print(f"Try Again \nscore: {target}")
   except ValueError:
      print("Invalid input, please enter a number!!")
      pass
   
   if (target == 10):
      print("You Win")
   





   
   
