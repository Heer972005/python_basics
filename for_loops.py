for item in 'python':
    print(item)
    
for item in ['heer','tiara','mehta']:
    print(item)
    
for item in[1,2,3,4,]:
    print(item)
print("\n")
for item in range(10):
    print(item)
print("\n")
for i in range(5,10):
    print(i)
print("\n")

for i in range(5,10,2):
    print(i)
    
#calculate the total
prices=[10,20,30]
total=0
for price in prices:
    total+=price
print(f"Total:{total}")

index=0;
while index<len(prices):
    total+=prices[index]
    index+=1
print(f"total:{total}")
print("total:",(total))