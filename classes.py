class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")
        
point1=Point()

point1.y=20
point1.x=10
point1.draw()
print(point1.x)
print(point1.y)
point2=Point()
point2.y=90
print(point2.y)