def main():
   name = input("whats your name? ")
   print(hi(name))

def hi(to="world"):
   return f"hi, {to}"

if __name__ == "__main__":
   main()