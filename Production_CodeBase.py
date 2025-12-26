class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return f"Persons name is {self.name}. He is leaving in {self.country}, and he is {age} old."    
        
p1 = Person("Tushar", "India", date(2000,1,1))
print(p1.calculate_age())


# Python program to create a calculator class. Include methods for basic arithmetic operations
class Calculator:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def addition(self):
        return f"Addition of {self.first_number} and {self.second_number} is {self.first_number + self.second_number}." 

    def subtraction(self):
        return f"Subtraction of {self.first_number} and {self.second_number} is {self.first_number - self.second_number}." 

    def multiplication(self):
        return f"Multiplication of {self.first_number} and {self.second_number} is {self.first_number * self.second_number}." 

    def division(self):
        return f"Division of {self.first_number} and {self.second_number} is {self.first_number / self.second_number}." 
    
c1 = Calculator(12,30)    
print(c1.addition())
print(c1.subtraction())
print(c1.multiplication())
print(c1.division())

# Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.  
class Shape:
    def __init__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"Area of Circle is {3.14*(self.radius**2)}"

    def perimeter(self):
        return f"Perimeter of Circle is {3.14*self.radius*2}"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return f"Area of rectangle is {self.length*self.width}."

    def perimeter(self):
        return f"Perimter of rectangle is {2*(self.length+self.width)}."

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return f"Area of Triangle is {0.5*self.base*self.height}."

    def perimeter(self):
        return f"Perimter of Triangle is {self.side1+self.side2+self.side3}."

print("--------------------------------------")
# Area and Perimter of Circle
s1 = Circle(7)
print("Area and Perimter of Circle")
print(s1.area())
print(s1.perimeter())
print("--------------------------------------")

# Area and Perimeter of Recatangle
r1 = Rectangle(3,5)
print("--------------------------------------")
print("Area and Perimter of Rectangle")
print(r1.area())
print(r1.perimeter())
print("--------------------------------------")

# Area and Perimeter of =Triangle
r1 = Triangle(3,5,2,2,2)
print("--------------------------------------")
print("Area and Perimter of Triangle")
print(r1.area())
print(r1.perimeter())
print("--------------------------------------")
              