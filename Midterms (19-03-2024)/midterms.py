students = {
   'Theodore': 19,
   'Roxanne': 22,
   'Mathew': 21,
   'Betty': 20
}

def key_in_dict(d, key):
   return True if key in d.keys() else False

print("\n Original dictionary elements:")
print(students)
print(key_in_dict(students, 'Roxanne'))
print(key_in_dict(students, 'Gina'))

