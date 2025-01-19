'''can  lists can contain heterogeneous data types and objects. 
For instance, integers, strings, and even functions can be stored within the same list.
'''
names=["heer","meet","nand","diya","mehta"]
#output-['heer', 'meet', 'nand', 'diya']
print(names)
print(names[2])
print(names[-2])
print(names[2:])#['nand', 'diya', 'mehta']
print(names[2:4])#['nand', 'diya']
print(names[2:-1])#['nand', 'diya']
print(names[-2:2])#[] as slicing is always left to right
print(names[:])
names[0]='hee'
print(names)