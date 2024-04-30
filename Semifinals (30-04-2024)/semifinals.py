import random 
import statistics
import sys
import requests
import json

coin = random.choice(['heads', 'tails'])
print(coin)

number = random.randint(1, 10)
print(number)

cards = ['jack', 'queen', 'king']
random.shuffle(cards)

for card in cards:
   print(card)
   
print(statistics.mean([100, 90]))

#sys.argv provides a way by which users can introduce information from the command line
#sys.exit provides a means by which the program can exit if the error arises
# if len(sys.argv) < 2:
#    sys.exit('Too few arguments')

# for arg in sys.argv[1:]:
#    print(f"hello, my name is {arg}")  

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))
   
o = response.json()
for result in o['results']:
   print(result['trackName'])