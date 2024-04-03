import randomizer as rand
import RPS as rps
import blackjack as bj

def get_user_choice():
    while True:
        user_choice = input(
            "========================================\n"
            "Enter the number of your choosing.\n"
            "1. Item Randomizer\n"
            "2. Rock Paper Scissors\n"
            "3. Black Jack\n"
            "4. Quit\n"
            "========================================\n"
        )
        if user_choice in ["1", "2", "3", "4"]:
            return user_choice
        else:
            print("ERROR: Not a valid choice. Enter either '1', '2', '3', or '4'\n")

def main():
    menu = True
    
    while menu:
        user_choice = get_user_choice()
        
        if user_choice == "1":
            print("[Item Randomizer]")
            rand.randomizer()
        elif user_choice == "2":
            print("[Rock Paper Scissors]")
            rps.RPS()
        elif user_choice == "3":
            print("[Black Jack]")
            bj.BJ()    
        else:
            menu = False
            print("Program Exit")
    
if __name__ == "__main__":
     main()
        