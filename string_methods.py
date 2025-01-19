course="tiara is cute"
       #012345678910
len1=len(course)
print(len1)
print(len(course))
upp=course.upper();
print(upp);
print(course.upper())
print(course.lower())
print(course.find('o'))#did not find the chracter so rreturns -1
print(course.find('t'))
print(course.find('a'))
print(course.find('is'))
print(course.find("is"))
ch=course.find('r')
ch1=course.find("r")
print(ch1)
print(ch)
print(course.replace('cute','cutie'))
#will not show error just will not replace anything, will just return the original string
print(course.replace('Cute','cutie'))
replace1=course.replace("cute",'cutie')
print(replace1)

#boolean expression-in course
flg='tiara'in course
print(flg)
print('tiara'in course)
print('Tiara'in course)
print()
print('a'in course)
print('A'in course)

print(course.title())
print(course)