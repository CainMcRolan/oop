from inflect import engine

p = engine()
name = []

while True:
   try:
      user_input = input("Name: ")
      name.append(user_input)
   except EOFError:
      break

if len(name) == 1:
   N = name[0]
elif len(name) == 2:
   N = p.join(name)
else:
   N = ", ".join(name[:-1]) + ", and " + name[-1]

print("Adieu, adieu, to " + N)