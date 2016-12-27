#exercise 17
#def is used for functions in python
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))

def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))
    
def print_one(arg1):
    print("arg1: %r" % (arg1))
    
def print_none():
    print("I got nothin'.")
    
print_two("Jaleel", "Savoy")
print_two_again("Jaleel", "Savoy")
print_one("Jaleel")
print_none()