message=input(">")
words=message.split(' ')
emojis={
    ":)":"Mr.best😊",
    ":(":"😔",
    "irrited":"😤",
    "happy":"😁"
}
output=""
for i in words:
    output+=emojis.get(i,i)+" "
print(output)
#print(words)