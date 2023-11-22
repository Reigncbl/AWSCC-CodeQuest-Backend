import os 

def end_game(result):
    if result == "win":
        print("\nCongratulations! You win!")
    else:
        print("Game over.")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def game_choice(prompt):
    while True:
        try:
            choice = int(input(prompt))
            if choice in [1, 2]:
                clear_terminal()
                return choice
            else:
                print("invalid input. enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():            
    print("Welcome to the Adventure Game!")
    print("you came across a split path to a cave and a forest. where do you go? ")
    print("1. Cave\n2. Forrest")

    choice = game_choice("Enter your choice (1 or 2): ")
    
    if choice == 1:
        print("\nyou entered the cave and you encountered a legde. what do you do? ")
        print("1. Jump\n2. Go around")

        choice = game_choice("Enter your choice (1 or 2): ")
        if choice == 1:
            print("You jump over the ledge.")
            print("You made it to the other side!")
            end_game("win")
        else:
            print("You got lost in the cave.")
            end_game("lose")
    elif choice == 2:
        print("\nyou entered the forest and you encountered a monster. what do you do? ")
        print("1. Fight\n2. Run")
        choice = game_choice("Enter your choice (1 or 2): ")
        if choice == 1:
            print("You defeated the monster!")
            end_game("win")
        else:
            print("The monster catches you.")
            end_game("lose")
    else:
        print("Invalid choice. Game over.")

if __name__ == "__main__":
    main()
