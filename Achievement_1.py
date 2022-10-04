#   This program will calculate the area of a circle,
#   square, or triangle. The program will launch into a
#   menu and the user will choose 1-4, with a shape matching 
#   each number and a quit option being assigned to
#   number 4. Depending on the shape user will input
#   the dimensions required for the calculation

calculationOptions = {
    1: 'Calculate the area of a circle',
    2: 'Calculate the area of a rectangle',
    3: 'Calculate the area of a triangle',
    4: 'Quit\n\n',
}

def printCalculations():
    for key in calculationOptions.keys():
        print (key, '--', calculationOptions[key] )

i = 1

while i == 1:

    print("Hello, welcome to geometryPal")
    print("[please note this program can only interperet numbers, and can only calculate right angle triangles]\n\n")

    printCalculations()

    choice = float(input("Which shape would you like to calculate?: "))

    if choice == 1:
        radius = float(input("What is the radius of your circle?: "))
        print("\n\nThe area of your circle is ", (3.14159*(radius**2)))
        print("The circumference of your circle is ", (2*3.14159*radius))
        exit()
    elif choice == 2:
        length = float(input("What is the length of your rectangle?: "))
        width = float(input("What is the width of your rectangle?: "))
        print("\n\nThe area of your rectagle is ", (length*width))
        print("The perimetere of the rectangle is ", ((length*2)+(width*2)))
        exit()
    elif choice == 3:
        a = float(input("What is the first side length of your triangle?: "))
        b = float(input("What is the second side length of your triangle?: "))
        c = (((a**2) + (b**2)) ** 0.5)
        print("The area of your right angle triangle is ", ((a*b)/2))
        print("The perimeter of your right angle triangle is ", (a + b + c))
        exit()
        
    elif choice == 4:
        print("goodbye")
        exit()

    else:  
        print("This is not a supported option, try again.")

