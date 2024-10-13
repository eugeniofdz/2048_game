from random import randint
import os

def start_game():
    # Game mat
    mat = [[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]
    
    # print insturctions
    print('''
        Commands are as follows : 
        'W' or 'w' : Move Up
        'S' or 's' : Move Down
        'A' or 'a' : Move Left
        'D' or 'd' : Move Right
    ''')

    #Add a random 2 in the math
    add_new_2(mat)
    return mat

def add_new_2(mat):
    #Get random mat position
    r = randint(0,3)
    c = randint(0,3)

    #If initial position already has number select a new random one
    while mat[r][c] != 0:
        r = randint(0,3)
        c = randint(0,3)

    #Add a two to an empty random index
    mat[r][c] = 2


def game_state(mat):
    # Check if player has won (2048 tile)
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'WON'
    
    # Check if there are any empty spaces (game not over)
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return ''  # Game not over, can still play
    
    # Check for possible merges horizontally or vertically
    for i in range(4):
        for j in range(3):
            # Check horizontal neighbors
            if mat[i][j] == mat[i][j + 1]:
                return ''
            # Check vertical neighbors
            if mat[j][i] == mat[j + 1][i]:
                return ''
    
    # If no empty spaces or possible merges, the game is lost
    return 'LOST'


def compress(mat):

    #position to compress
    pos = 0

    #True if there is a change
    changed = False

    #New mat to return
    new_mat = [[0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0]]

    for i in range(4):
        #Reset position to 0 for next row
        pos = 0
        for j in range(4):
            #If there is a num change it to the correct position
            if mat[i][j] != 0:
                #compress left
                new_mat[i][pos] = mat[i][j]

                pos += 1
                #To prevent if number is already in the correct position
                if j != pos:
                    changed = True

    return new_mat, changed


def mergere(mat):

    #True if changed
    changed = False

    #loop through array
    for i in range(4):
        for j in range(3):
            #if next number is the same double the left number and replace right number to 0
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j + 1] = 0
                changed = True
    
    return mat, changed


def reversed(mat):

    #new mat to return
    new_mat = []

    #Append new empty rows to new mat
    for i in range(4):
        new_mat.append([])
        #appends last item in mat to new row
        for j in range(4):
            new_mat[i].append(mat[i][3 - j])

    return new_mat


def transpose(mat):
    #New mat to return
    new_mat = []

    #Append new empty rows to new mat
    for i in range(4):
        new_mat.append([])
        #Append switched row and column to desired row and column
        for j in range(4):
            new_mat[i].append(mat[j][i])

    return new_mat


def move_left(mat):

    #First compress mat
    new_mat, changed1 = compress(mat)

    #Next merge mat
    new_mat, changed2 = mergere(new_mat)

    #If mat was chaanged in any of both methods
    changed = changed1 or changed2

    #Recompress mat and a temp value just to meet the return statement
    new_mat, temp = compress(new_mat)

    return new_mat, changed

def move_right(mat):

    #reverse mat
    new_mat = reversed(mat)
    
    #Move left
    new_mat, changed = move_left(new_mat)

    #Now reverse mat again to show correct position
    new_mat = reversed(new_mat)

    return new_mat, changed


def move_up(mat):

    #Transpose mat
    new_mat = transpose(mat)

    #same thing as move left
    new_mat, changed = move_left(new_mat)

    #Transpose mat again
    new_mat = transpose(new_mat)

    return new_mat, changed


def move_down(mat):

    #Transpose mat
    new_mat = transpose(mat)

    #Same thing as move right
    new_mat, changed = move_right(new_mat)

    #transpose again
    new_mat = transpose(new_mat)

    return new_mat, changed


def clear_screen():
    # Clear the terminal screen based on the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS/Linux
        os.system('clear')


def print_grid(mat):
    print("+----+----+----+----+")  # Top border
    for row in mat:
        row_str = "|".join(f"{num:^4}" if num != 0 else "    " for num in row)  # Center-align each number
        print(f"|{row_str}|")
        print("+----+----+----+----+")  # Separator after each row
