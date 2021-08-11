"""
CONNECT 4

by @andresdeinnocentiis

"""

from colorama import Fore


class Board(object):
    def __init__(self):
        pass
    
    def createBoard(self):
        board = []
        for line in range(15):
            row = []
            if line % 2 != 0:
                for column in range(15):
                    if column % 2 != 0:
                        row.append("   ")
                    else:
                        row.append("|")
            
            else:
                for column in range(15):
                    if column % 2 != 0:
                        row.append("---")
                    else:
                        row.append("-")
                #row.append("-----")
            board.append(row)
                
        return board

    def convertString(self, board):
        board_str = ""
        for row in board:
            for column in row:
                board_str += column
            board_str += "\n"
            
        return board_str
    
    
class Player:
    def __init__(self, name = ""):
        self.__name: name
        
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name    
        
    def choose_piece(self):
        piece = (input("Choose the piece you would like to play with (X / O): ")).upper()
        while piece != "X" and piece != "O":
            print("The piece you've picked does not exist. Please choose again.")
            piece = (input("Choose the piece you would like to play with (X / O): ")).upper()
        
        return piece    
 
 
    def pick_column(self):
        chose = False
        while not chose:
            try:
                pickColumn = int(input("Please choose the column where you'd like to place your piece (1, 2, 3, 4, 5, 6 or 7): "))
                while pickColumn not in range (1,8):
                    print("Error. Invalid range.")
                    pickColumn = int(input("Please choose the column where you'd like to place your piece (1, 2, 3, 4, 5, 6 or 7): "))
                chose = True
                if pickColumn != 1:
                    pickColumn += (pickColumn - 1)
            except:
                print("Value Error. you can only enter an int Value.")
            
            
            
        return pickColumn
 
 
def check_for_victory(board, row, column):
    victory = False
    try:
        #CHECKEO VICTORIA EN HORIZONTAL:
        if (board[row][column] == board[row][column-2]) and (board[row][column] == board[row][column-4]) and (board[row][column] == board[row][column-6]):
            victory = True
        if (board[row][column] == board[row][column-2]) and (board[row][column] == board[row][column-4]) and (board[row][column] == board[row][column+2]):
            victory = True
        if (board[row][column] == board[row][column-2]) and (board[row][column] == board[row][column+4]) and (board[row][column] == board[row][column+2]):
            victory = True
        if (board[row][column] == board[row][column+2]) and (board[row][column] == board[row][column+4]) and (board[row][column] == board[row][column+6]):
            victory = True
        #CHECKEO VICTORIA EN VERTICAL:
        if (board[row][column] == board[row+2][column]) and (board[row][column] == board[row+4][column]) and (board[row][column] == board[row+6][column]):
            victory = True
        #CHECKEO VICTORIA EN DIAGONAL DERECHA:
        if (board[row][column] == board[row+2][column+2]) and (board[row][column] == board[row+4][column+4]) and (board[row][column] == board[row+6][column+6]):
            victory = True
        if (board[row][column] == board[row+2][column+2]) and (board[row][column] == board[row+4][column+4]) and (board[row][column] == board[row-2][column-2]):
            victory = True
        if (board[row][column] == board[row+2][column+2]) and (board[row][column] == board[row-4][column-4]) and (board[row][column] == board[row-2][column-2]):
            victory = True
        if (board[row][column] == board[row-2][column-2]) and (board[row][column] == board[row-4][column-4]) and (board[row][column] == board[row-6][column-6]):
            victory = True
        #CHECKEO VICTORIA EN DIAGONAL IZQUIERDA:
        if (board[row][column] == board[row+2][column-2]) and (board[row][column] == board[row+4][column-4]) and (board[row][column] == board[row+6][column-6]):
            victory = True
        if (board[row][column] == board[row+2][column-2]) and (board[row][column] == board[row+4][column-4]) and (board[row][column] == board[row-2][column+2]):
            victory = True
        if (board[row][column] == board[row+2][column-2]) and (board[row][column] == board[row-4][column+4]) and (board[row][column] == board[row-2][column+2]):
            victory = True
        if (board[row][column] == board[row+2][column-2]) and (board[row][column] == board[row+4][column-4]) and (board[row][column] == board[row+6][column-6]):
            victory = True
    except:
        pass              
    return victory
    
    
    
    
def main():
    player1 = Player()
    player1.set_name(input("Enter the name for the Player 1: "))
    piece1 = Fore.RED + player1.choose_piece() + Fore.RESET
    piece2 = ""
    if "X" in piece1:
        piece2 = Fore.BLUE + "O" + Fore.RESET
    else:
        piece2 = Fore.BLUE + "X" + Fore.RESET
        
    player2 = Player()
    player2.set_name(input("Enter the name for the Player 2: "))
    print("\n")
    
    board = Board().createBoard()
   
    boardstr = Board().convertString(board)
    print(boardstr)
    
    print("\n")
    
    endgame = False
    move1 = False
    move2 = False
    space = False
    while not endgame:
        while not move1:
            player = player1.get_name()
            print(f"It's {player}'s turn:\n")
            column = player1.pick_column()
            row = -2
            print("\n")
            
            if board[row][column] == "   ":
                board[row][column] = f" {piece1} "
                move1 = True
                move2 = False
            else:
                space = False  
                while not space:    
                    try:
                        row -= 2
                        if board[row][column] == "   ":
                            board[row][column] = f" {piece1} "
                            space = True
                            move1 = True
                            move2 = False
                    except:
                        print("Error. Out of range.")
                        space = True
                        
              
                 
                
                    
            
            boardstr = Board().convertString(board)
        
        print(boardstr)
        print("\n")  
        victory = check_for_victory(board, row, column)    
        if victory:
            print(f"{player1.get_name()} WINS. FLAWLESS VICTORY! {player2.get_name()} HAS BEEN HUMILIATED.\n")
            print(f"{player1.get_name()} Is the real MVP. {player2.get_name()} should try his luck doing some other stuff.")
            print("\n")
            break
            move2 = True
            endgame = True
              
            
            
                
        while not move2:
            player = player2.get_name()
            print(f"It's {player}'s turn:\n")
            column = player2.pick_column()
            row = -2
            print("\n")
            if board[row][column] == "   ":
                board[row][column] = f" {piece2} "
                
                move2 = True              
                move1 = False
            else:    
                space = False  
                while not space:
                    try:    
                        row -= 2
                        if board[row][column] == "   ":
                            board[row][column] = f" {piece2} "
                            space = True
                            move2 = True
                            move1 = False
                    except:
                        print("Error. Out of range.")
                        space = True
                
            
            
            boardstr = Board().convertString(board)
            
        print(boardstr)
        print("\n") 
        victory = check_for_victory(board, row, column)    
        if victory:
            print(f"{player2.get_name()} WINS. FLAWLESS VICTORY! {player1.get_name()} HAS BEEN HUMILIATED.\n")
            print(f"{player2.get_name()} Is the real MVP. {player1.get_name()} should try his luck doing some other stuff.")
            print("\n")
            break
            move1 = True
            endgame = True
        
            
main()