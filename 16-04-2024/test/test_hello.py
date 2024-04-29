from hi import hi

def test_default():
   assert hi() == "hi, world"

def test_argument():
   assert hi("David") == "hi, David"