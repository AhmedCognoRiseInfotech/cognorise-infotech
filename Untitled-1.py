#1
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice (1/2/3/4): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid choice")
#2
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User Input 
length = int(input("Enter the desired length of the password: "))
print("Generated Password:", generate_password(length))

import random

def play_rps():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Select rock, paper, or scissors: ").lower()
    computer_choice = random.choice(choices)
    
    print("Computer chose:", computer_choice)
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

# Play Again Logic 3
score_user = 0
score_computer = 0
while True:
    result = play_rps()
    print(result)
    if "win" in result:
        score_user += 1
    elif "lose" in result:
        score_computer += 1
    print(f"Score - You: {score_user}, Computer: {score_computer}")
    
    if input("Play again? (yes/no): ").lower() != 'yes':
        break
# 4
import random

def hangman():
    word_list = ['python', 'java', 'ruby', 'javascript']
    word = random.choice(word_list)
    guessed = '_' * len(word)
    attempts = 6
    guessed_letters = []

    while attempts > 0 and '_' in guessed:
        print("Current word:", guessed)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        guessed_letters.append(guess)

        if guess in word:
            guessed = ''.join([letter if letter == guess or letter in guessed_letters else '_' for letter in word])
        else:
            attempts -= 1
            print("Incorrect! Attempts left:", attempts)

    if '_' not in guessed:
        print("Congratulations! You've guessed the word:", word)
    else:
        print("Game Over! The word was:", word)

# Play Again Logic
while True:
    hangman()
    if input("Play again? (yes/no): ").lower() != 'yes':
        break
#5
import random

def roll_dice(sides, rolls):
    results = [random.randint(1, sides) for _ in range(rolls)]
    return results

# User Input
sides = int(input("Enter the number of sides on the dice: "))
rolls = int(input("Enter the number of rolls: "))
print("Dice Roll Results:", roll_dice(sides, rolls))
#6
import tkinter as tk
import time

def countdown(count):
    if count >= 0:
        mins, secs = divmod(count, 60)
        timer_display['text'] = f"{mins:02d}:{secs:02d}"
        root.update()
        time.sleep(1)
        countdown(count - 1)
    else:
        timer_display['text'] = "Time's up!"

def start_timer():
    total_seconds = int(entry.get())
    countdown(total_seconds)

# GUI Setup
root = tk.Tk()
root.title("Countdown Timer")

timer_display = tk.Label(root, font=('Helvetica', 48))
timer_display.pack()

entry = tk.Entry(root)
entry.pack()

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack()

root.mainloop()
