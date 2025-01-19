'''def greet_user():
    print("hi there!")
    print("Welcome abord")

print("Start")
greet_user()
greet_user()
print("Stop")'''

'''#parameters are holes or placeholders
def greet_user(name):
    print(f"Hi {name}!")
    print("Welcome aboard")
print("start")
#arguments are actual pieces of information that we supply to these functions
greet_user("heer")
greet_user("tiara")
print("finish")'''

def greet_user(first_name,last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")
print("start")
#arguments are actual pieces of information that we supply to these functions
greet_user(last_name="heer",first_name="mehta") #keyword argument
greet_user("tiara","cutie")#positional arguments
#if mixing positional and keyword arguments
#then first positional and keyword vice-versa not applicable
print("finish")

#return
def squre(number):
    print(number*number)
print(squre(3))#return 9 and none cause default value of fn is none

def square(number):
    return(number*number)

print(square(3))