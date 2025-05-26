# number guessing game programmed by Matrix Studios in 2025
import random
while True:
    number_choice = int(input("Choose a number from 1-10: "))
    computer_choice = random.randint(1,10)
    Sure = input("Are you sure of your answer kid? (y/n)").lower()
    if number_choice == computer_choice:
        print("You guess the correct number :D")
        print("thank you for playing :D")
        print("Programmed by Matrix on the 25th of May 2025")
    if Sure == "n":
        print("Then you are not fit to play the game then....")
        progress = input("Would you like to keep playing??(y/n): ").lower()
        if progress == "n":
         print("thank you for playing :D")
         print("Programmed by Matrix on the 25th of May 2025")
         break
    
        
    elif number_choice > computer_choice:
        print("The number you picked is higher than the actual number XD, Good try Kid")
        progress = input("Would you like to keep playing??(y/n): ").lower()
        if progress == "n":
            print("thank you for playing :D")
            print("Programmed by Matrix on the 25th of May 2025")
            break
    
    elif number_choice < computer_choice:
        print("The number you picked is lower than the actual number XD, Good try Kid")
        progress = input("Would you like to keep playing??(y/n): ").lower()
        if progress == "n":
         print("thank you for playing :D")
         print("Programmed by Matrix on the 25th of May 2025")
         break
  
    
        
    else:
        print("Kindly put an appropriate figure")
        progress = input("Would you like to keep playing??(y/n): ").lower()
        if progress == "n":
         print("thank you for playing :D")
         print("Programmed by Matrix on the 25th of May 2025")
         break
    