#tictactoe gameboard display
def gameboard(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    print(f"  {p1}  | {p2} | {p3}  ")
    print(" -------------")
    print(f"  {p4}  | {p5} | {p6}  ")
    print(" -------------")
    print(f"  {p7}  | {p8} | {p9}  ")

# Initialize empty spaces for the board
pos1 = pos2 = pos3 = pos4 = pos5 = pos6 = pos7 = pos8 = pos9 = " "

# Call the function to display the empty board initially
gameboard(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9)

# Explaining which player is X and which player is O
print("Player 1 is X and Player 2 is O!")

#defining the first player as X
player= "X"

#running the game until all spots are filled or if someone wins
while pos1== " " or pos2== " " or pos3== " " or pos4== " " or pos5== " " or pos6== " " or pos7== " " or pos8== " " or pos9== " ":
        move=input(f"Player {player} what position would you like to play? ")

        if move=="1" and pos1==" ":
                pos1 = player
        elif move=="2" and pos2==" ":
                pos2 = player
        elif move=="3" and pos3==" ":
                pos3 = player
        elif move=="4" and pos4==" ":
                pos4 = player
        elif move=="5" and pos5==" ":
                pos5 = player
        elif move=="6" and pos6==" ":
                pos6 = player
        elif move=="7" and pos7==" ":
                pos7 = player
        elif move=="8" and pos8==" ":
                pos8 = player
        elif move=="9" and pos9==" ":
                pos9 = player
        else: 
                print ("Invalid move choose a different number")
                #allowing replay for invalid move
                if player=="X":
                        player="O:"
                elif player=="O":
                        player="X" 
        # checking for a winner
        if (pos1==pos2==pos3==player) or (pos4==pos5==pos6==player) or (pos7==pos8==pos9==player) or (pos1==pos5==pos9==player) or (pos3==pos5==pos7==player) or (pos1==pos4==pos7==player) or (pos2==pos5==pos8==player) or (pos3==pos6==pos9==player):
                print()
                print(f"Player {player} wins!")
                break # if theres a winner stop the game

        # checking for a draw
        if pos1!= " " and pos2!= " " and pos3!= " " and pos4!= " " and pos5!= " " and pos6!= " " and pos7!= " " and pos8!= " " and pos9!= " ":
                print()
                print("Its a Draw! Do a rematch!")
                break #stop the game
                
        # switching players from X to O
        if player=="X":
                player="O"
        else:
                player="X"

        # Call the function again to display the updated board
        gameboard(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9)

