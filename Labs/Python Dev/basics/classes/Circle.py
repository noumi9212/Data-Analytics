class Circle():
    pi = 3.14
    def __init__(self, radius=1):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * Circle.pi
    def set_radius(self, new_radius):
        self.radius = new_radius
    def get_radius(self):
        return self.radius
    def print(self):
        print(f"This circle has radius of {self.radius} and area of {self.area()}")
r = float(input("Please Enter radius to draw a circle: "))
myCircle = Circle(r)
myCircle.print()
