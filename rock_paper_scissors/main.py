import random

print("Welcome to the Rock, Paper, Scissors game!")

choices = ["rock", "paper", "scissors"]
user_score = computer_score = 0
print("Let's play!")

while True:
    user_input = input("Type Rock, Paper, Scissors or Q to quit: ").lower()
    
    if user_input == 'q':
        print(f"\nFinal score - You: {user_score}, Computer: {computer_score}")
        print("Thanks for playing!")
        break

    if user_input not in choices:
        print("Invalid input. Please try again.\n")
        continue

    computer_input = random.choice(choices)
    print(f"Computer chose: {computer_input}.")

    if user_input == computer_input:
        print("It's a tie!")
    elif (user_input == "rock" and computer_input == "scissors") or \
         (user_input == "paper" and computer_input == "rock") or \
         (user_input == "scissors" and computer_input == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print(f"Current Score - You: {user_score}, Computer: {computer_score}\n")
