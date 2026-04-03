#Guessing Game tkinter version
import tkinter as tk
import random


root = tk.Tk()
root.title("My Guessing Game")
root.geometry("400x300")


secret_number = None
lives = 0


def start_game():
    global secret_number, lives

    
    difficulty = difficulty_var.get()

    
    if difficulty == "Easy":
        secret_number = random.randint(1, 10)
        lives = 10
    elif difficulty == "Medium":
        secret_number = random.randint(1, 15)
        lives = 5
    elif difficulty == "Hard":
        secret_number = random.randint(1, 25)
        lives = 3
    elif difficulty == "Impossible":
        secret_number = random.randint(1, 100)
        lives = 1

   
    message_label.config(text=f"Game started! You have {lives} lives.\nGuess a number!")
    lives_label.config(text=f"Lives: {lives}")
    guess_entry.config(state="normal")
    submit_button.config(state="normal")

def check_guess():
    global lives
    try:
        guess = int(guess_entry.get())
    except ValueError:
        message_label.config(text="Please enter a valid number!")
        return

    if guess == secret_number:
        message_label.config(text=f"🎉 Congrats! You guessed the number {secret_number}!")
        guess_entry.config(state="disabled")
        submit_button.config(state="disabled")
    else:
        lives -= 1
        if guess < secret_number:
            message_label.config(text="Hint: The number is higher!")
        else:
            message_label.config(text="Hint: The number is lower!")

        lives_label.config(text=f"Lives: {lives}")

        if lives == 0:
            message_label.config(text=f"😢 Game over! The number was {secret_number}.")
            guess_entry.config(state="disabled")
            submit_button.config(state="disabled")

    
    guess_entry.delete(0, tk.END)


welcome_label = tk.Label(root, text="Welcome to My Guessing Game!", font=("Arial", 16))
welcome_label.pack(pady=10)


difficulty_var = tk.StringVar(value="Easy")
difficulty_frame = tk.Frame(root)
difficulty_frame.pack(pady=5)

for level in ["Easy", "Medium", "Hard", "Impossible"]:
    tk.Radiobutton(difficulty_frame, text=level, variable=difficulty_var, value=level).pack(side="left")


start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack(pady=10)


message_label = tk.Label(root, text="Select difficulty and start the game.", font=("Arial", 12))
message_label.pack(pady=5)


lives_label = tk.Label(root, text="Lives: 0", font=("Arial", 12))
lives_label.pack(pady=5)


guess_entry = tk.Entry(root, state="disabled")
guess_entry.pack(pady=5)


submit_button = tk.Button(root, text="Submit Guess", state="disabled", command=check_guess)
submit_button.pack(pady=10)

root.mainloop()





#Guessing Game Terminal Version
"""import random
import tkinter


root = tkinter.Tk()  
root.title("My Guessing Game")
root.geometry("400x300")

label = tkinter.Label(root, text="Welcome to my guessing game!", font=("Arial", 16))
label.pack(pady=20)

label.config("Welcome to Random Number Generator")
print("Please select the following dificulty")
print("1 - Easy (1 - 10)  2 - Medium (1 - 15)  3 - Hard (1 - 25)  4 - Impossible (1 - 100)")

n = random.randint(1, 50)
difficultySelect = int(input("Please select the dificulty: "))


if difficultySelect == 1:
    print("You have selected easy difficutly")
    lives = 0 + 10
    print(f"You now have {lives} lives to start with!")

elif difficultySelect == 2:
    print("You have selected Medium difficutly")
    lives = 0 + 5
    print(f"You now have {lives} lives to start with!")

elif difficultySelect == 3:
    print("You have selected Hard difficutly")
    lives = 0 + 3
    print(f"You now have {lives} lives to start with!")

elif difficultySelect == 4:
    print("You have selected Imopssible difficutly")
    lives = 0 + 1
    print(f"You now have {lives} life to start with!")


print("Please guess a number between 1 and 50")
while lives > 0:
    guess = int(input("Your guess: "))

    if guess == n:
        print ("ggs, you've completed the game and won congrats")
        break

    elif guess < n:
        print("Hint: The number you seek is higher")
        lives = lives - 1
        print (f"You now have {lives} lives left!")

    elif guess > n:
        print("Hint: The number you seek is lower")
        lives = lives - 1
        print (f"You now have {lives} lives left!")


if lives == 0:
    print(f"The number you were seeking was {n}")
    print("game over!")
    print("press ESC to exit!")


root.mainloop()"""