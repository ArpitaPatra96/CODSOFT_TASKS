import random

print("===== Rock Paper Scissors Game =====")

choices = ["rock", "paper", "scissors"]

while True:

    user = input("\nEnter Rock, Paper or Scissors: ").lower()

    if user not in choices:
        print("Invalid Choice! Try Again.")
        continue

    computer = random.choice(choices)

    print("Your Choice :", user)
    print("Computer Choice :", computer)

    if user == computer:
        print("Result : It's a Tie!")

    elif user == "rock" and computer == "scissors":
        print("Result : You Win!")

    elif user == "paper" and computer == "rock":
        print("Result : You Win!")

    elif user == "scissors" and computer == "paper":
        print("Result : You Win!")

    else:
        print("Result : Computer Wins!")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThank You for Playing!")
        break