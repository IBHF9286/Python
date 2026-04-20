#super() is used to call the parent class's method from the child class. It allows you to access and invoke methods of the parent class without explicitly naming it.

class Shape():
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"A {self.color} colored shape that is {'filled' if self.is_filled else 'not filled'}.")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        self.radius = radius
        super().__init__(color, is_filled)  

    def describe(self):
        print("Area of the circle is:", 3.14 * self.radius ** 2)

        super().describe()  # Call the parent class's describe method to get the shape description

class Square(Shape):
    def __init__(self, color, is_filled, side_length):
        self.side_length = side_length
        super().__init__(color, is_filled)  

    def describe(self):
        print("Area of the square is:", self.side_length ** 2)

        super().describe()  # Call the parent class's describe method to get the shape description

class Triangle(Shape):
    def __init__(self, color, is_filled, base, height):
        self.base = base
        self.height = height
        super().__init__(color, is_filled)

    def describe(self):
        print("Area of the triangle is:", 0.5 * self.base * self.height)

        super().describe()  # Call the parent class's describe method to get the shape description

#create instances of the shapes
circle = Circle("red", True, 5)
square = Square("blue", False, 4)
triangle = Triangle("green", True, 6, 3)

#describe the shapes
circle.describe()
square.describe()
triangle.describe()


