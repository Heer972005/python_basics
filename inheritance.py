'''inheritance-'''
class Mammal:
    def walk(self):
        print("walk")
class Dog(Mammal):
    def bark(self):
        print("Bark")
        #pass#keyword-pass this line
        #used as python does not like empty class

class Cat(Mammal):
    #pass
    def be_ann(self):
        print("Annoying")

dog1=Dog()
dog1.walk()
dog1.bark()
cat1=Cat()
cat1.be_ann()
cat1.walk()