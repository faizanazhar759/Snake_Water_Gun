def game_result(player_choice, computer_choice):
    options = ["Snake", "Water", "Gun"]
    result = ""

    if player_choice == computer_choice:
        result = "It's a draw!"
    elif (player_choice == "Snake" and computer_choice == "Water") or \
         (player_choice == "Water" and computer_choice == "Gun") or \
         (player_choice == "Gun" and computer_choice == "Snake"):
        result = "You Win!"
    else:
        result = "You Lose!"
    
    return result
