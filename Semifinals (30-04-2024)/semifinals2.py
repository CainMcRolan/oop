from my_calculator import square

def main():
   test_square()
   
def test_square():
   assert square(2) == 4, 'error!!!'
   assert square(3) == 9
   
main()