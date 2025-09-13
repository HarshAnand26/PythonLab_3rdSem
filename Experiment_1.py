# Student Name : [Harsh Anand]
# Roll Number  : [2024UG4015]
# Course       : CS-2101 / CD-2101 - Python Programming Lab

# Task - 1 : Swapping of two numbers

# Code to swap two numbers

a = int(input("Enter a: "))
b = int(input("Enter b: "))

a , b = b , a 

print("After Swapping\na = " , a , "\nb = " , b)



# Task - 2 : Computation of student marks

# Code to print grades of students according to marks

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
    
elif marks >= 80:
    print("Grade B")

elif marks >= 70:
    print("Grade C")

elif marks >= 60:
    print("Grade D")

else:
    print("Fail")



# Task - 3 : Calculation of area and perimeter of a rectangle.

# Code to calculate area and perimeter of rectangle

length = int(input("Enter length of rectangle: "))
breadth = int(input("Enter breadth of rectangle: "))

Perimeter = 2 * (length + breadth)
Area = length * breadth

print("It's Area is: " , Area , "\nIt's Perimeter is: " , Perimeter)



# Task - 4 : Input two complex numbers and display their sum , difference and product

# Code to input two complex numbers and calculate their sum , difference and product

c1 = complex(input("Enter 1st complex number: "))
c2 = complex(input("Enter 2nd complex number: "))

sum = c1 + c2 
difference = c1 - c2 
product = c1 * c2

print("1st complex number: " , c1)
print("2nd complex number: " , c2)
print("Their sum: " , sum)
print("Their difference: " , difference)
print("Their product: " , product)



# Task - 5 : a) Convert temperature from celsius to farhenheit

# Code to convert temperature from celsius to farhenheit

Celsius = float(input("Enter temperature in celsius: "))

Farhenheit = (9/5 * Celsius) + 32

print("Temperature in Celsius is: " , Celsius)
print("Temperature in Farhenheit is: " , Farhenheit)


# b) Convert temperature from farhenheit to celsius

Farhenheit = float(input("Enter temperature in farhenheit: "))

Celsius = ((Farhenheit - 32)*5)/9

print("Temperature in Farhenheit is: " , Farhenheit)
print("Temperature in Celsius is: " , Celsius)







