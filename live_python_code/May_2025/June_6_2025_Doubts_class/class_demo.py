def area_of_circle(radius):
    return 3.14 * radius * radius

area = area_of_circle(5)
print(f"The area of the circle with radius 5 is: {area}")

area = area_of_circle(10)
print(f"The area of the circle with radius 5 is: {area}")

area = area_of_circle(15)
print(f"The area of the circle with radius 5 is: {area}")

#####################################################

class Circle:
    """A class to represent a circle."""
    def __init__(self, radius):
        self.radius = radius

    def circle_area(self):
        return 3.14 * self.radius * self.radius
    
    def circle_circumference(self):
        return 2 * 3.14 * self.radius
    
    def circle_diameter(self):
        return 2 * self.radius
    
    def circle_info(self):
        return f"Circle with radius {self.radius}, area {self.circle_area()}, circumference {self.circle_circumference()}, diameter {self.circle_diameter()}"
    
    def circle_perimeter(self):
        return self.circle_circumference()
    

    
circle1 = Circle(5)
print(f"The area of the circle with radius {circle1.radius} is: {circle1.area()}")

circle2 = Circle(10)
print(f"The area of the circle with radius {circle2.radius} is: {circle2.area()}")

#########################

class Rectangle:
    """A class to represent a rectangle."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangle_area(self):
        return self.length * self.width
    
    def rectangle_perimeter(self):
        return 2 * (self.length + self.width)
    
    def rectangle_info(self):
        return f"Rectangle with length {self.length}, width {self.width}, area {self.area()}, perimeter {self.perimeter()}"




def circle_area(radius):
    """Calculate the area of a circle."""

    if radius <= 0:
        return 3.14 * radius * radius
    else:
        return "Radius must be a positive number."
    
