'''constructor-it is a function that gets
called at the time of creating an object'''

class Point:
    #init-short of initialised
    #init-fn or the method that gets called
    #when we create a new point object
    #self-is a reference to the current object
    '''when we create a new point object 
    self references that object in memory, the same
    object, that we were referencing using the variable'''
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point=Point(10,20)
print(point.x)