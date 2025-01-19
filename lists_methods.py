numbers=[5,2,1,7,4]
numbers.append(13)#just take one argument
print(numbers)

numbers.insert(0,10)
numbers.insert(2,6)
print(numbers)

numbers.remove(5)#will show error if number not found
print(numbers)
numbers.remove(2)
print(numbers)

print(numbers.pop())# gives output-13
print(numbers)
print()

print(numbers.index(6))#will show error if number not found

print(50 in numbers)#returns boolean value if not found-false

print(numbers.count(5))#will show 0 if not found

numbers.insert(3,6)
print(numbers)

print(numbers.count(6))

print(numbers.sort())#will reuturn-none
# none-is a object in python that represents absence of value
numbers.sort()#sorts in ascending 
print(numbers)

#print(numbers.reverse())#in descending #will also return none
numbers.reverse()
print(numbers)

nms=numbers.copy()
print(numbers.copy())#this works
print(nms)

numbers.sort()
print(numbers)

numbers.clear()
print(numbers)
print(numbers.clear())
print(numbers)