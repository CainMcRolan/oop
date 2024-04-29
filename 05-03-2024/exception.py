def main():
   x = get_int("What's X")
   print(f"x is {x}")


def get_int(prompt):
   while True:
      try:
         return int(input(prompt))
      except ValueError:
         pass
  
main()