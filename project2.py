import random
computer_choice = random.randint(1,100)

print(90*'-','Number Guessing Game','-'*89)
print("Welcome to Number guessing game!")
choice = input("Do you want to play it(yes/no): ").lower()

if choice == 'yes':
    tries = 0 

    while True:
        try:
            player_choice = int(input("Enter your choice (1-100): "))
        except ValueError:
            print("please enter valid choice")
            continue

        if player_choice < 1 or player_choice >100:
            print("please enter number between 1-100")
            continue

        tries += 1
        if player_choice > computer_choice:
            print('choose smaller number.')
            continue
        elif player_choice < computer_choice:
            print('choose larger number.')
            continue
        else:
            print(f"Congratulations! you won the game in {tries} try.")
            break
    print("Thank you for playing this game. \nSee you soon.")
    
elif choice == 'no':
    print("its okay! see you again.")
else:
    print("you haven't enter valid input! exiting the game.")