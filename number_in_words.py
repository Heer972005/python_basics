phone=input("Phone: ")
keys={
    "1":"ONE",
    "2":"TWO",
    "3":"THREE",
    "4":"FOUR"
}
output=""
for i in phone:
    output+=keys.get(i,"!")+" "

print(output)