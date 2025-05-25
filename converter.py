print("Press enter to skip ahead to the unit you are looking for")
print("Note:This is a beta version its not perfect and is under development!!!!!")
UNIT = input("Choose an option to convert: 1. Speed 2. Weight 3. Distance 4. Temperature")
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
    distance = int(input("Distance: "))
    unit = input("(K)Kilometers or (M)meters: ")
    if unit.upper() == "K":
        converted = distance * 1000
        print("distance in meters: " + str(converted))
    else:
        converted = distance / 1000
        print("distance in kilometers: " + str(converted))
elif UNIT == "5":
 temperature = int(input("Temperature: "))
 unit = input("(F)ahreneit or (C)elsius: ")
 if unit.upper() == "F":
    converted = temperature / 33.8
    print("Temperature in celsius: " + str(converted))
 else:
    converted = temperature * 33.8
    print("Temperature in Fahrenheit: " + str(converted))
print("Thanks for using my converter")
