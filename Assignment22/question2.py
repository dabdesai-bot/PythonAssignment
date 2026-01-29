class Circle:
    PI=3.14

    def __init__(self):
        self.radius=0.0
        self.area=0.0
        self.circumference=0.0
        print("Inside Constructor")

    def Accept(self):
        self.radius=float(input("Enter the number"))

    def CalculateArea(self):
        self.area=Circle.PI*self.radius*self.radius

    def Calculatecircumference(self):
        self.circumference= 2*Circle.PI*self.radius

    def Display(self):
        print("The Radius of Circle:",self.radius)
        print("The Area of Circle:",self.area)
        print("The Circumference of Circle:",self.circumference)
        print("---------------------------------------")

obj1=Circle()
obj2=Circle()

obj1.Accept()
obj1.CalculateArea()
obj1.Calculatecircumference()
obj1.Display()

obj2.Accept()
obj2.CalculateArea()
obj2.Calculatecircumference()
obj2.Display()



