player1 = input("Player1: ")
player2 = input("Player2: ")

if(player1.lower == player2.lower):
    print("Draw!")

elif(player1.lower == "rock" and player2.lower == "scissor") or \
    (player1.lower == "scissor" and player2.lower == "paper") or \
    (player1.lower == "paper" and player2.lower == "rock"):
    print("Player1 wins!")

else:
    print("Player2 wins!")