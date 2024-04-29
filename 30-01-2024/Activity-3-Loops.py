#Write a code that will display the following output
#Use Loop and Conditionals

for i in range(7):
   print("&" * (7 - i), end ="")
   for j in range(i):
      print(j + 1, end="")
   print(i + 1)