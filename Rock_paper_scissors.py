#-----------------------------------------Rock paper scissors game-----------------------------------

import random

# Starting scores for the user and computer
user_score = 0
computer_score = 0

while True:
    # User input
    print("\nWelcome to Rock, Paper, Scissors game")
    print("Choose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    user_choice = int(input("Enter the number corresponding to your choice: "))

    # Validate user input
    if user_choice < 1 or user_choice > 3:
        print("Invalid choice. Please choose a number between 1 and 3.")
        continue

    # Map user's choice to 'rock', 'paper', or 'scissors'
    moves = ['rock', 'paper', 'scissors']
    user_move = moves[user_choice - 1]

    # Generate a random choice for the computer
    computer_choice = random.choice(moves)

    # Display user's choice and computer's choice
    print(f'You chose: {user_move}')
    print(f'Computer chose: {computer_choice}')

    # Determine the winner
    if user_move == computer_choice:
        print("It's a tie!")
 
    # rock vs paper=>paper wins
    # rock vs scissor=>rock wins
    # paper vs scissor=>scissor wins
  
    
    elif (user_move == 'rock' and computer_choice == 'scissors') or \
         (user_move == 'paper' and computer_choice == 'rock') or \
         (user_move == 'scissors' and computer_choice == 'paper'):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    # Display the current score
    print(f"Your score: {user_score}")
    print(f"Computer's score: {computer_score}")

    #  if the user wants to play another round
    another_round = input("Do you want to play another round? (y/n): ")
    if another_round.lower() != "y":
        break

print("Thanks for playing!")