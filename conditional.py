#take=input("Enter true or false:")
'''take=False
if take:
    print("it's a hot day")
    print("Drink water")
    
else:
    print("It's a cold day")
    print("Wear warm clothes")
print("Enjoy!")'''

'''is_hot=False
is_cold=True
if is_hot:
    print("it's a hot day")
    print("Drink water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy!")'''

price=1000000
x=int(input("Enter credit"))
if x==10:
    down_payment=0.1*price
else:
    down_payment=0.2*price
    
print(f"Down payment:${down_payment}")