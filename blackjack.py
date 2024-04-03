import random

# Black Jack - The dealer will have 2 cards (1 close and 1 open (1-11))
# - The player will have 2 cards (both open from 1-11)
# - The player will choose between HIT or STAND, HIT - will draw a card (1-9) while STAND (Dealer will reveal all cards till it reaches 18 or more)

def get_user_move():
    while True:
        user_move = input("[1. HIT | 2. STAND | 3. See Rules]: ").lower()
        
        if user_move in ["hit", "stand", "rules", "1", "2", "3"]:
            return user_move
        else:    
            print("ERROR: Not a valid move.\n"
                  "Enter either 'hit', 'stand', 'rules', '1'(to hit), '2'(to stand), or '3' to see the rules\n")
            
def get_user_choice():
    while True:
        user_choice = input("[1. Play again | 2. Exit]: ")
        if user_choice in ["1", "2"]:
            return user_choice
        else:
            print("ERROR: Not a valid choice. Enter either '1' or '2'\n")
            
def get_rules():
    print("[Black Jack Rules]\n"
          "- At the start, you will have 2 revealed cards while the dealer has only 1 revealed card (1 - 11).\n"
          "- The move [HIT] you'll get a random card from 1 - 9 unlike the start, \nThe goal is to have your card sum up to as close as 21 but not OVER or you'll lose.\n"
          "- The move [STAND] means you're content to what you have and you're ready to see the dealer's unrevealed cards\n"
          "- In order to win without a BUST is to have your cards be higher than the dealer's and no more than 21.\n"
          )
            
def BJ():
    
    BJ_active = True
    while BJ_active:
        print("========================================\n")
        
        playBJ()
        user_choice = get_user_choice()
        
        if user_choice == "1":
            print("[PLAY AGAIN]")
        elif user_choice == "2":
            BJ_active = False
    
def playBJ():
    
    user_cards = []
    dealer_cards = []
    
    #starting cards of the player and the dealer    
    user_cards.append(draw_card("start"))
    user_cards.append(draw_card("start"))
    dealer_cards.append(draw_card("start"))
        
    print(f"Dealer's Card: {dealer_cards}\n"
        f"Your Card: {user_cards}\n"
        f"[You: {sum(user_cards)} | Dealer: {sum(dealer_cards)}]")
    
    playBJ_active = True
    while playBJ_active:

        user_move = get_user_move()
        
        #player's moves conditions
        if user_move == "1" or user_move == "hit".lower():
            print("You chose to HIT!\n")
            user_cards.append(draw_card(""))
        elif user_move == "2" or user_move == "stand".lower():
            print("You chose to STAND!\n")
            dealer_cards = dealer_reveal(dealer_cards)
            playBJ_active = False
        elif user_move == "3" or user_move == "rules".lower():
            get_rules()
        
        #display current cards    
        print(f"Dealer's Card: {dealer_cards}\n"
            f"Your Card: {user_cards}\n"
            f"[You: {sum(user_cards)} | Dealer: {sum(dealer_cards)}]")
        
        #perfect win or lose conditions
        if sum(user_cards) == 21:
            print("THAT'S BLACKJACK! YOU WON!\n")
            return
        elif sum(user_cards) > 21:
            print("IT'S A BUST! YOU LOSE!\n")
            return
        
        
        
    #win and lose conditions
    if sum(user_cards) > sum(dealer_cards) or sum(dealer_cards) > 21:
        print("Congrats! You win!")
        return
    elif sum(user_cards) < sum(dealer_cards) or sum(user_cards) > 21:
        print("Pay up! You lose!")
        return
    else:
        print("It's a DRAW!")        
            
        
def draw_card(x):
    if x == "start":
        return random.randint(1, 11)
    else:
        return random.randint(1, 9)

def dealer_reveal(dealer_cards):
    dealer_active = True
    while dealer_active:
        dealer_cards.append(draw_card(""))
        
        if sum(dealer_cards) >= 18:
            return dealer_cards
    
