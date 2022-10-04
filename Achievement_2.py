#   This program calculates the area and perimeter of the shape desired. It will begin by launching a menu with 4 options.
#   These options include circle, square, rectangle and quit. The calculations will be performed by functions which return the results
#   back to the calling print. A strip feature will be included in the lines so that if a user accidnetally enters '   1' it will still function.

calculationOptions = {
    1: 'Calculate the area of a circle',
    2: 'Calculate the area of a rectangle',
    3: 'Calculate the area of a square',
    4: 'Quit\n\n',
}

def printCalculations():
    for key in calculationOptions.keys():
        print (key, '--', calculationOptions[key] )

def rectangleArea():
    return length * width

def rectanglePerimeter():
    return (length * 2) + (width * 2)

def circleArea():
    return (3.14159 * (radius ** 2))

def circlePerimeter():
    return (2 * 3.14159 * radius)

def squarePerimeter():
    return 4 * a

def squareArea():
    return a * a

i = 1

while i == 1:

    print("Hello, welcome to geometryPal")
    print("[please note this program can only interperet numbers]\n\n")

    printCalculations()

    choice = int(input("Which shape would you like to calculate?: ").strip())

    if choice == 1:
        radius = float(input("What is the radius of your circle?: ").strip())
        print("\n\nThe area of your circle is ", eval('circleArea()'), ' cm\u00b2')
        print("The circumference of your circle is ", eval('circlePerimeter()'), 'cm')

        exit()

    elif choice == 2:
        length = float(input("What is the length of your rectangle?: ").strip())
        width = float(input("What is the width of your rectangle?: ").strip())
        print("\n\nThe area of your rectagle is ", eval('rectangleArea()'), ' cm\u00b2')
        print("The perimetere of the rectangle is ", eval('rectanglePerimeter()'), 'cm')

        exit()

    elif choice == 3:
        a = float(input("What is the dimension of your square?: ").strip())
        print('The Area of your square is ', eval('squareArea()'), ' cm\u00b2')
        print('The perimeter of your square is ', eval('squarePerimeter()'), ' cm')
        

        exit()
        
    elif choice == 4:
        print("goodbye")

        exit()

    else:  
        print("This is not a supported option, try again.")
