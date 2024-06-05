print("==================")
print("Area Calculator")
print("==================")

def area_of_circle(radius):
    return 3.14159 * radius ** 2

def area_of_rectangle(length, width):
    return length * width

def area_of_square(side):
    return side ** 2

def area_of_triangle(base, height):
    return 0.5 * base * height

def quit():
    print("Goodbye!")
    exit()

ip=int(input(" 1 for Circle \n 2 for Rectangle\n 3 for Square\n 4 for Triangle\n 5 to Quit: \n"))
if ip==1:
    radius = float(input("Enter the radius of the circle: "))
    print("The area of the circle is: ", area_of_circle(radius))
elif ip==2:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    print("The area of the rectangle is: ", area_of_rectangle(length, width))
elif ip==3:
    side = float(input("Enter the side of the square: "))
    print("The area of the square is: ", area_of_square(side))
elif ip==4:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    print("The area of the triangle is: ", area_of_triangle(base, height))
elif ip==5:
    quit()
