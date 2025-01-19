def emoji_converter(message):
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
    return output

message=input(">")
print(emoji_converter(message))