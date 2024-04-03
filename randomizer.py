import random

#Randomizer - gives 1 outcome entered by the user minimum 2 and maximum 5
def randomizer():
    print("========================================\n")
    items = []
    activeRandomizer = True
    while activeRandomizer:
        user_input = input("How many things to randomize? (Maximum 5)\n")
        #Input check (only accepts numbers)
        try: 
            user_intput = int(user_input)
            
            if user_intput > 1 and user_intput <= 5:
                i = 1
                while i <= user_intput:
                    item_input = input(f"Enter the {i}/{user_input} of the items\n")
                    items.append(item_input)
                    i += 1
                selected_item = random.choice(items)
                print(f"Items: {items}")
                print(f"Outcome: {selected_item}")
                
                #continue or exit
                i = True
                while i:
                    user_choice = input("[1. Reroll | 2. Reset | 3. Exit]\n")
                    #Reroll
                    if user_choice == "1":
                        selected_item = random.choice(items)
                        print(f"Items: {items}")
                        print(f"Outcome: {selected_item}")
                    #Reset    
                    elif user_choice == "2":
                        items.clear()
                        i = False
                    #Exit    
                    elif user_choice == "3":
                        print("Program Exit")
                        activeRandomizer = False
                        i = False
                        
                    else:
                        print("Invalid Entry, try again\n")    
            else:
                print(
                    "Invalid input, you must only put\n" 
                    "atleast 2 and max of 5 items to randomize\n"
                    )
            
        except ValueError:
            print("ERROR: Enter a number only.")
        