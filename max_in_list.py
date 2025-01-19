numbers=[3,6,2,8,4,]#comma will not show syntax error
'''The comma after the last element (4,) is optional.
Python interprets it as if the list ends after the last value (4).
This feature is particularly useful for formatting multi-line lists 
or when adding/removing elements from lists to avoid accidental syntax issues.'''
max=numbers[0]
for i in numbers:
    if(i>max):
        max=i
print(max)
