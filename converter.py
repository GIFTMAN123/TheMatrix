# Programmed by Matrix 2024, last updated 2025
print("Python Program to convert various units")
print("Note:This is a beta version its not perfect and is under development!!!!!")
UNIT = input("Choose an option to convert: 1. Speed 2. Weight 3. Height 4. Temperature")
if UNIT == "1":
     Speed = int(input("speed: "))
     unit = input("(M)ph or (K)ph: ")
     if unit.upper() == "M":
      converted = Speed * 1.6092
      print("Speed in Kph: " + str(converted))
     else:
      converted = Speed / 1.6092
      print("Speed in mph: " + str(converted))
elif UNIT == "2":
     weight = int(input("Weight: "))
     unit = input("(K)g or (L)bs: ")
     if unit.upper() == "K":
       converted = weight / 0.45
       print("Weight in Lbs: " + str(converted))
     else:
      converted = weight * 0.45
      print("Weight in Kgs: " + str(converted))
elif UNIT =="3":
    height = float(input("Height: "))
    unit = input("(C)Centimeters or (F)Feet: ")
    if unit.upper() == "F":
        converted = height / 0.032808
        print("height in centimeters: " + str(converted))
    else:
        converted = height * 0.032808
        print("height in feet: " + str(converted))
elif UNIT == "5":
 temperature = int(input("Temperature: "))
 unit = input("(F)ahreneit or (C)elsius: ")
 if unit.upper() == "F":
    converted = temperature / 33.8
    print("Temperature in celsius: " + str(converted))
 else:
    converted = temperature * 33.8
    print("Temperature in Fahrenheit: " + str(converted))
Progress = input("Would you like to convert another unit?(y/n) ").lower()
if Progress == "n":
 print("Thanks for using my converter")
elif Progress == "y":
 print("Then restart the program bruv")
else:
    print("GET OU-")