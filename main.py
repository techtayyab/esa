def circle(radius):
    return 3.14 * radius * radius

if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle: "))
    print("The area of the circle is:", circle(radius))