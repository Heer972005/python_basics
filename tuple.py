#tuple-are immutable
#only 2 methods-to just get info but cannot change
numbers=(1,2,3,2)
#numbers[0]=10#will generate error as cannot mutate
print(numbers[0])
print(numbers.count(2))
print(numbers.index(1))
print(numbers.index(2))
