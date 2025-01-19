matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])
matrix[0][1]=30
print(matrix[0][1])

for row in matrix:
    for col in row:
        print(col)

print()        
x=0
while(x<len(matrix)):
    y=0
    while(y<len(matrix[x])):
        print(matrix[x][y])
        y+=1
    x+=1
        