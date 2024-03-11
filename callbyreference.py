string = "geeks"
def test(string):
    string = "geeksforgeeks"
    print("Inside Function:", string)
test(id(string))
print("Outside Function:", string)