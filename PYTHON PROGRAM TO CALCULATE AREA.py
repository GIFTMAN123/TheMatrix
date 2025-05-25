print("Program to calculate area or circumference of a circle")
OPERATION = input("Choose your operation, 1. Area 2. Circumference")
if OPERATION == "1":
    print("You have chosen Area input the parameters below")
    Radius = int(input("Radius: "))
    Area = Radius * Radius * 22/7
    print("The Area is: " + str(Area) + "cm square")
    print("======================================================================================")
elif OPERATION == "2":
    print("You have chosen Perimeter pls input the parameters below")
    Radius_2 = int(input("Radius: "))
    Circumference = 2 * 22/7 * Radius_2
    print("The perimeter of the circle is:" + str(Circumference) + "centimeters")
