
board = ["-","-","-",
         "-","-","-",
         "-","-","-",
        ]

def display_board(board):
    print( board[0] + "  | "+ board[1] + "  | "+ board[2] )
    print("------------")
    print( board[3] + "  | "+ board[4] + "  | "+ board[5] )
    print("------------")
    print( board[6] + "  | "+ board[7] + "  | "+ board[8] )
    
def check_winning_conditions(board):
    player_1 = "X"
    player_2 = "O"
    if board[0]==board[1]==board[2]==player_1 or board[0]==board[1]==board[2]==player_2:  # winning_conditions for rows  !!!!!!!!!
        return True
    elif board[3]==board[4]==board[5]==player_1 or board[3]==board[4]==board[5]==player_2:
        return True  
    elif board[6]==board[7]==board[8]==player_1 or board[6]==board[7]==board[8]==player_2:
        return True  
    elif board[0]==board[3]==board[6]==player_1 or board[0]==board[3]==board[6]==player_2: # winning_conditions for Columns !!!!!!!!!!
        return True  
    elif board[1]==board[4]==board[7]==player_1 or board[1]==board[4]==board[7]==player_2:
        return True  
    elif board[2]==board[5]==board[8]==player_1 or board[2]==board[5]==board[8]==player_2:
        return True  
    elif board[0]==board[4]==board[8]==player_1 or board[0]==board[4]==board[8]==player_2: # winning_conditions for Diagonals !!!!!!!!!!
        return True  
    elif board[2]==board[4]==board[6]==player_1 or board[2]==board[4]==board[6]==player_2:
        return True  
    else:
        return False
    
def inp(board):
    x = int(input("Enter the position 1-9 ==>"))
    if board[x-1]!="-":
        print(" value already exist")
        return inp(board)
    else:
        return x 

player1 = input("Enter the player 1 name ==>")
player2 = input("Enter the player 2 name ==>")
display_board(board)

for i in range(9):
    if i%2==0:
        x = inp(board)
        board[x-1]="X"
        display_board(board)
        if check_winning_conditions(board):
            print(" player X is win 🥳🥳🥳")
            break
    else:
        x = inp(board)
        board[x-1]="O"
        display_board(board)
        if check_winning_conditions(board):
          print(" player O is win 🥳🥳🥳")
          break

    