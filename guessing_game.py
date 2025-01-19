number=9
count=0
limit=3
while count<limit:
    guess=int(input('Guess:'))
    count+=1;
    if(guess==number):
        print('you won')
        break
else:
    print("You failed")
    
    
    