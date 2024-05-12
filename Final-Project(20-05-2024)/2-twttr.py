def main():
   try:
      text = input("Input: ")
   except EOFError:
      print("Invalid Input")
      return
   
   letters = ['a', 'e', 'i', 'o', 'u']
   output = ''
   for c in text:
      if c.lower() not in letters:
         output += c
   print(output)

main()