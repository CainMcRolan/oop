def main():
   try:
      greeting = input("Greeting: ").strip().lower()
      print(["$100", "$20", "$0"][greeting.startswith("h") + greeting.startswith("hello")])
   except (IndexError, ValueError):
      print("Invalid Input")
      
main()