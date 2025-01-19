for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

numbers=[2,2,2,2,5]
for x in numbers:
    output=""
    for y in range(x):
        output+="x"
    print(output)