# Matrix's Attempt to create rock paper scissors python program Beta program was created by Matrix then used Mosh to
# guide and understand main concepts i.e Loop system, Choice injection Copyright 2025 Matrix Studios
import random
item = {'r': 'Rock', 's' : 'Scissors', 'p': 'Paper'}
choice = "r, s , p"
while True:
    user_choice = input("Rock(r). Scissors(s), Paper(p): ").lower()
    if user_choice not in choice:
     print("Invalid option please choose an option")
     continue
    computer_choice = random.choice(choice)
    print(f"You chose:{item[user_choice]}")
    print(f"Computer chose:{item[computer_choice]}")
    if user_choice == computer_choice:
        print("Tie, Good game")
    elif user_choice == 'r' and computer_choice == 's':
        print("You win, Beginner's luck")
    elif user_choice == 'r' and computer_choice == 'p':
        print("Computer wins, Good game mate")
    elif user_choice == 'p' and computer_choice == 's':
        print("Computer wins, Good game")
    elif user_choice == 'p' and computer_choice == 'r':
        print("You win congrats but don't get excited its beginner's luck")
    elif user_choice == 's' and computer_choice == 'r':
        print("I dunno who wins lets call it a tie")
    elif user_choice == 's' and computer_choice == 'p':
        print("Beginner's luck kid")
    progress = input("Do you want to continue???? y/n ").lower()
    if progress == "n":
        print("Alright bye kid beat ya next time")
        break