import random

def get_computer_choice(difficulty):
    options = ["Snake", "Water", "Gun"]

    if difficulty == "Easy":
        return random.choice(options)
    elif difficulty == "Medium":
        # Slight bias towards water
        return random.choice(["Snake", "Water", "Water", "Gun"])
    elif difficulty == "Hard":
        # Bias towards gun to make it harder for the player
        return random.choice(["Gun", "Gun", "Snake"])
    else:
        # Default to a random choice if difficulty is invalid
        return random.choice(options)
