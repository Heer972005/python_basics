customer={
    #here name,age,is_verified is known as key
    "name":"Tiara cute",
    "age":5,
    #"age":3,interpreter-so line by line-so if same name of key then last will be taken
    "is_verified":True
}
print(customer["name"])
#print(customer["Name"])# shows error-KeyError: 'Name'
print(customer.get("name"))
print(customer.get("Name"))#does not show error-gives "None"
print(customer.get("Name","Heer"))#can supply default value
print(customer.get("age"))
customer["name"]="tiara cutie"
print(customer["name"])
customer["date"]="9th jan"
print(customer.get("date"))

