name=input("Enter the name:")
len1=len(name)
if(len1<3):
    print("enter alteast 3 characters")
elif(len1>50):
    print("maximum 50 is possible")
else:
    print("looks good")