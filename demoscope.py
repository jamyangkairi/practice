# def myfunc():
#   x = 300
#   def myinnerfunc():
#     print(x)
#   myinnerfunc()
# myfunc()

# x = 300
# def myfunc():
#     print(x)
# myfunc()
# print(x)

def myfunc_global():
    global x
    x = 300
myfunc_global()
print(x)