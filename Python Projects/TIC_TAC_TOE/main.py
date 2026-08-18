from random import randint

'''##################### User Input #########################''' 
def marker_choice():
    """Allows user to choose 'x' or 'o' and returns tuple with player1 and player2 markers."""
    while True:    
        marker = input("Please pick a marker 'x' or 'o': ")
        if marker == 'x':
            # Player1 gets 'x', Player2 gets 'o'
            return ('x','o')
        elif marker == 'o':
            # Player1 gets 'o', Player2 gets 'x'
            return ('o','x')
        else:
            # Invalid input - ask again
            print("Invalid Input Try Again")

           

'''##################### Display Board ######################'''
def display_board(board):
    """Prints the current state of the Tic-Tac-Toe board.
    Board positions are numbered 1-9:
    7 | 8 | 9
    4 | 5 | 6
    1 | 2 | 3
    """
    print(board[7] + " |" + board[8] + " |" + board[9])
    print("--" + "|" + "--" + "|" + "--")
    print(board[4] + " |" + board[5] + " |" + board[6])
    print("--" + "|" + "--" + "|" + "--")
    print(board[1] + " |" + board[2] + " |" + board[3])


'''##################### Marker Placer ######################'''
def marker_placer(board, marker, position):
    """Places the player's marker ('x' or 'o') at the specified position on the board."""
    board[position] = marker


'''##################### WIN Check ##########################'''
def win_check(board, mark):
    """Checks if the given marker has achieved a winning combination.
    Checks all 8 possible winning combinations:
    - 3 rows
    - 3 columns
    - 2 diagonals
    """
    if ((board[1]== mark and board[2]== mark and board[3] == mark) or  # Row 1
         (board[4]== mark and board[5]== mark and board[6] == mark) or  # Row 2
         (board[7]== mark and board[8]== mark and board[9] == mark) or  # Row 3
         (board[1]== mark and board[4]== mark and board[7] == mark) or  # Column 1
         (board[2]== mark and board[5]== mark and board[8] == mark) or  # Column 2
         (board[3]== mark and board[6]== mark and board[9] == mark) or  # Column 3
         (board[1]== mark and board[5]== mark and board[9] == mark) or  # Diagonal (top-left to bottom-right)
         (board[7]== mark and board[5]== mark and board[3] == mark) ):  # Diagonal (bottom-left to top-right)
         return True
    else:
        return False

'''###################### Choose First ######################'''
def choose_first():
    """Randomly decides which player goes first.
    Returns 'player1' or 'player2'.
    """
    choose = randint(1,2)
    if (choose == 1):
        return 'player1'
    else:
        return 'player2'
    
'''###################### Space Check & Full Check #######################'''
def space_check(board, position):
    """Checks if a specific position on the board is empty (available).
    Returns True if empty, False if occupied.
    """
    return board[position] == ' '

def full_check(board, position):
    """Checks if the board is completely full (no more empty spaces).
    Returns True if board is full (draw), False if there are empty spaces.
    """
    for i in range(1,10):
       if (space_check(board, i) == True):  # Found an empty space
           return False  # Board is not full
    return True  # All spaces are filled

'''###################### Player Choice ###############################'''
def player_choice(board):
    """Gets a valid position from the player.
    Validates that the position (1-9) is empty before returning.
    Loops until valid input is received.
    """
    while True:
        position = input("Choose the next position from (1 to 9):\n")
        if space_check(board, int(position)):  # Check if position is empty
            return int(position)
        elif not position.isdigit():  # Check if input is not a number
            print("Invalid Input, try again")
        else:
            # Position already occupied - ask for a different one
            print("Invalid Position, try again")

'''######################## Replay ###############################'''
def replay():
    """Asks the player if they want to play another game.
    Returns True to play again, False to quit.
    """
    re = input("Do you want to play again: 'Y' or 'N' ")
    if re.lower() == 'y':  # Yes - play again
        return True
    else:  # No or any other input - quit
        return False
    

'''########################## Main ##################################'''
# Display welcome message and show board layout
print("%%%%%%%%%%%% WELCOME %%%%%%%%%%%%%%")
board = ['#','1','2','3','4','5','6','7','8','9']
print("\nBoard positions:")
display_board(board)

# Initialize empty board for gameplay
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

# Get player markers and display them
(player1, player2) = marker_choice()
print(f"Player-1:{player1}\nPlayer-2:{player2}")

# Randomly choose who goes first
first_player = choose_first()
if first_player == 'player1':
    marker = player1  # Use the actual marker character ('x' or 'o')
else:
    marker = player2  # Use the actual marker character ('x' or 'o')
print(f"\n{first_player} goes first\n")
game_on = True

# Main game loop
while game_on:
    # Display whose turn it is
    if marker == player1:
        print("Player-1's turn")
    else:
        print("Player-2's turn")
    
    # Get valid position from current player
    position = player_choice(board)
    
    # Place the marker on the board
    marker_placer(board, marker, position)
    
    # Display updated board
    display_board(board)
    
    # Check if current player won
    if win_check(board, marker):
        display_board(board)
        winner = "Player-1" if marker == player1 else "Player-2"
        print(f"{winner} WINS")
        # Ask if players want to play again
        if replay():
            # Reset board and choose new first player
            board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            first_player = choose_first()
            if first_player == 'player1':
                marker = player1
            else:
                marker = player2
            print(f"{first_player} goes first")
        else:
            # Exit game
            game_on = False
    
    # Check if board is full (draw/tie)
    elif full_check(board, position):
        print("Game Over, It's a DRAW")
        # Ask if players want to play again
        if replay():
            # Reset board and choose new first player
            board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            first_player = choose_first()
            if first_player == 'player1':
                marker = player1
            else:
                marker = player2
            print(f"{first_player} goes first")
        else:
            # Exit game
            game_on = False
    
    else:
        # No winner yet and board not full - switch to other player
        if marker == player1:
            marker = player2
        else:
            marker = player1
