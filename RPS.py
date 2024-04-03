import random
            
#validates user's move
def get_user_move():
    while True:
        user_move = input("Type your move (rock, paper, scissors): ").lower()
        
        if user_move in ["rock", "paper", "scissors"]:
            return user_move
        else:    
            print("ERROR: Not a valid move\n")
            
def get_user_choice():
    while True:
        user_choice = input("[1. Play again | 2. Exit]: ")
        if user_choice in ["1", "2"]:
            return user_choice
        else:
            print("ERROR: Not a valid choice. Enter either '1' or '2'\n")
 
#gameplay and determines winner           
def RPS_play():
    user_score = 0
    comp_score = 0 
    round = 1
    while round <= 3:
        user_move = get_user_move()
        comp_move = random.choice(["rock", "paper", "scissors"])

        #round winner
        if user_move == comp_move:
            print("ROUND DRAW!\n")
        elif user_move == "rock" and comp_move == "scissors" or \
            user_move == "paper" and comp_move == "rock" or \
            user_move == "scissors" and comp_move == "paper":
            user_score += 1
            print(f"ROUND {round}: You win!\n")
            round += 1
        else:
            comp_score += 1
            print(f"ROUND {round}: Computer wins!\n")
            round += 1
            
        print(
            f"YOU: {user_move}\n"
            f"COMPUTER: {comp_move}\n"
            f"SCORES: [You: {user_score} | Computer: {comp_score}]\n"
            )
        
        #game winner
        if user_score == 2 and comp_score == 0:
            print("GAME: [PERFECT WIN] You won the game!")
            return "user won"
        elif comp_score == 2 and user_score == 0:
            print("GAME: [PERFECT LOSE] Computer won the game!")
            return 
    if user_score > comp_score:
        print("GAME: Congrats! You won the game!")
        return "user won"
    else:
        print("GAME: You lose! Computer wins!")   
        return 
    
#continue or exit to game menu
def RPS():
    print("========================================\n")
    print("Rock, Paper, Scissors Rules:\n"
                        "-> Best out of 3!\n"
                        "-> Type your move (rock, paper, scissors)\n")
    RPS_active = True
    user_gamescore = 0
    comp_gamescore = 0
    while RPS_active:
        
        
        if RPS_play() == "user won":
            user_gamescore += 1
        else:
            comp_gamescore += 1
        
        print(f"GAME STANDING: [You: {user_gamescore} | Computer: {comp_gamescore}]\n")
        
        user_choice = get_user_choice()
        
        if user_choice == "1":
            print("[PLAY AGAIN]")
        elif user_choice == "2":
            RPS_active = False
        
        
            
        
        
            
        
            
    
    