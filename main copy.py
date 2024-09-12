import tkinter as tk
from game_logic import game_result
from difficulty_levels import get_computer_choice
from PIL import Image, ImageTk
#git config --global user.email "faizanazhar12@gmail.com"
#git config --global user.name "faizanazhar759"
# Sound effects (ensure 'wins' and 'lose' sounds exist in assets/sounds)
import pygame
pygame.mixer.init()

# Initialize scores globally
player_score = 0
computer_score = 0

def play_sound(result):
    if result == "You Win!":
        pygame.mixer.Sound("assets/sounds/win.wav").play()
    elif result == "You Lose!":
        pygame.mixer.Sound("assets/sounds/lose.wav").play()
    else:
        pygame.mixer.Sound("assets/sounds/draw.wav").play()

def update_gui(player_choice):
    global player_score, computer_score  # Allow modification of global score variables
    computer_choice = get_computer_choice(difficulty.get())

    # Ensure that computer_choice is valid (it can’t be None)
    if computer_choice is None:
        computer_choice_label.config(text="Error: Invalid difficulty setting")
        return

    result = game_result(player_choice, computer_choice)
    play_sound(result)

    # Update scores based on the result
    if result == "You Win!":
        player_score += 1
    elif result == "You Lose!":
        computer_score += 1

    # Update the GUI with the computer's choice and result
    computer_choice_label.config(text="Computer chose: " + computer_choice)
    result_label.config(text=result)
    update_score()

def update_score():
    score_label.config(text=f"Player: {player_score}   Computer: {computer_score}")

# Initialize main window
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("500x400")

# Difficulty setting
difficulty = tk.StringVar(root)
difficulty.set("Easy")  # Default difficulty level

# Load images
snake_img = ImageTk.PhotoImage(Image.open("assets/images/snake.png"))
water_img = ImageTk.PhotoImage(Image.open("assets/images/water.png"))
gun_img = ImageTk.PhotoImage(Image.open("assets/images/gun.png"))

# Buttons with images
snake_button = tk.Button(root, image=snake_img, command=lambda: update_gui("Snake"))
snake_button.pack(pady=10)

water_button = tk.Button(root, image=water_img, command=lambda: update_gui("Water"))
water_button.pack(pady=10)

gun_button = tk.Button(root, image=gun_img, command=lambda: update_gui("Gun"))
gun_button.pack(pady=10)

# Labels for computer's choice and result
computer_choice_label = tk.Label(root, text="Computer chose: ", font=("Arial", 12))
computer_choice_label.pack(pady=10)

result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)

# Difficulty level
difficulty_label = tk.Label(root, text="Choose Difficulty:", font=("Arial", 12))
difficulty_label.pack(pady=10)
difficulty_menu = tk.OptionMenu(root, difficulty, "Easy", "Medium", "Hard")
difficulty_menu.pack()

# Scoreboard
score_label = tk.Label(root, text=f"Player: {player_score}   Computer: {computer_score}", font=("Arial", 12))
score_label.pack(pady=20)

# Start the Tkinter loop
root.mainloop()
