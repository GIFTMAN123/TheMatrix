print("CALCULATOR PROGRAM(PYTHON)")
print("============================")
while True:
    OPERATION = input("Pls Choose an operation. 1. Addition 2. Subtraction 3. Division 4. Multiplication ")
    if OPERATION == "1":
        print("You have chosen Addition")
        first_number = input("First number: ")
        second_number = input("Second number: ")
        Sum = float(first_number) + float(second_number)
        print(Sum)
        Progress = input("Would you like to perform a different operation??(y/n)").lower()
        if Progress == "n":
         print("Thank You for using my calculator :D ")
         break
    elif OPERATION == "2":
        print("Subtraction")
        num_1 = input("first number: ")
        num_2 = input("second number: ")
        Subtraction = float(num_1) - float(num_2)
        print(Subtraction)
        Progress = input("Would you like to perform a different operation??(y/n)").lower()
        if Progress == "n":
         print("Thank You for using my calculator :D ")
         break
    elif OPERATION == "3":
        print("DIVISION")
        num_3 = input("first_number: ")
        num_4 = input("Second number: ")
        Division = float(num_3) / float(num_4)
        print(Division)
        Progress = input("Would you like to perform a different operation??(y/n)").lower()
        if Progress == "n":
         print("Thank You for using my calculator :D ")
         break
    elif OPERATION == "4":
        print("Multiplication")
        num_5 = input("first number: ")
        num_6 = input("Second number: ")
        Multiplication = float(num_5) * float(num_6)
        print(Multiplication)
        Progress = input("Would you like to perform a different operation??(y/n)").lower()
        if Progress == "n":
         print("Thank You for using my calculator :D ")
         break
    else:
        print("Pls rerun the code and pick a proper option")
