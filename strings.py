#course='Python's course for beginners'-will show error
#course="Python for "beginners"""-will show error

#for multiple line string-'''  '''
course='''
hi heer,

first string
thank you,
zxcv
'''
chara='herr gytv'
print(course)
print(chara[0])
'''negative index-gives charcter from last'''
print(chara[-1])
print(chara[0:3])#exclusive index 3 so from 0-2 
print(chara[2:])#exclusive of 2
print(chara[:2])#exclusive of 2
print(chara[:])#interpreter will assume 0 to end index
# therefore cloning can be done with this operator
clone=chara[:]
print('clone:'+clone);
print(chara[1:-1])


