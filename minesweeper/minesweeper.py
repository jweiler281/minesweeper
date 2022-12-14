import random
import pprint
mine_loc = []
field = []
dim = 10
mines = 10



def setup():
    # Initial config of the game dimensions and number of mines
    global dim
    # Will be updated, dimension of playing field (dim x dim)
    global mines
    # Will be updated, number of mines
    dim_ready = False
    # Input validation check that dimension is within confines
    mine_ready = False
    # Input validation check that number of mines is within confines
    dim_in = int(input("Enter dimensions for playing field (min2, max 10, default is 10): "))
    # Receive input on dimensions of playing field
    # TO DO: catch and handle error if no number is input or non-integer is input
    if dim_in < 2 or dim_in > 10:
    # Validate dimension given by input
        dim_ready = False
    else:
        dim_ready = True
    mines_in = int(input("Enter number of mines (cannot exceed 75% of playing field, default is 10): "))
    # Receive input on number of mines
    # TO DO: catch and handle error if no number is input or non-integer is input
    #max_mines = (dim_in * dim_in) * .75
    if mines_in < 0 or mines_in > (dim_in * dim_in) * .75:
    # Validate mines given by input
        mine_ready = False
    else:
        mine_ready = True
    if dim_ready == True and mine_ready == True:
    # If dimension and mines within constraints, reassign global variables for game
        dim = dim_in
        mines = mines_in
        return 0
    else:
        setup()

def mine_setup(): 
# create list with mine location coordinates
    while len(mine_loc) != mines: 
    # iterate until mine_loc list has dictated amount of mines
        mine = [random.randint(1, (dim)), random.randint(1, (dim))]
        # randomly pick mine coordinates up to dictated dimensions
        # mines [x, y]
        if mine not in mine_loc:
        # ensure there are no duplicates
            mine_loc.append(mine) 
            # append if not already in list
    return mine_loc

def guess():
# Takes player's guesses
    gx_ready = False
    # Validator of whether x value is within constraints
    gy_ready = False
    # Validator of whether y value is within constraints
    gy = int(input("What is your next guess Y-axis component?: ")) - 1
    # Receive input on x component
    if gy < 0 or gy >= (dim):
    # Validate x component is within constraints
        gy_ready = False
    else:
        gy_ready = True
    gx = int(input("What is your next guess X-axis component?: ")) - 1
    # Receive input on y component
    if gx < 0 or gx >= (dim):
    # Validate y component is within constraints
        gx_ready = False
    else:
        gx_ready = True
    if gx_ready == True and gy_ready == True:
    # If x/y components within constraints, return (x, y) tuple
        return (gy, gx)
    else:
    # If x/y components not within constraints, recurse to try again
        return (-1)

def start_field():
# Creates field to track mines, squares, and guesses
    global field
    # Tracks status of field and mines
    mine_symbol = 0
    # Annotates mine on field
    field = [[[-1,0] for k in range(dim)] for j in range(dim)]
    # Creates field with [[dim]dim] nested list
    # [-1(not mined) or 0(mined) or 1+(how many mined neighbors), 0(not visible) or 1(visible to player)]
    counter = 0
    while counter != (mines):
        field[int(mine_loc[counter][1]) - 1][int(mine_loc[counter][0]) - 1][0] = mine_symbol
        # Sets mine locations to 0 -- field[y][x]
        counter += 1
    return field_pretty()

def field_pretty():
# Prints field in more pretty grid
    global field
    header_row = list(range(1, dim + 1))
    field_output = "C:  " + str(header_row) + "\n"
    for i in range(dim):
        field_output = field_output + "R" + str(i + 1) + ": " + str(field[i]) + "\n"
    return field_output

def aligner():
    # Annotates squares 1 space from mines
    global field
    i = j = 0
    while i != dim:
    # Iterates through y axis
        y_counter = i
        j = 0
        while j != dim:
        # Iterates through x axis
            neighbors = [False, False, False, False, False, False, False, False]
            # Tracks which neighbor squares are mined
            # 0  1  2
            # 7  s  3
            # 6  5  4
            square_sum = 0
            # Number to set for square based on mined neighbors
            if field[y_counter][j][0] == 0:
            # Ignores square if mined
                neighbors[0] = False
            elif i == 0 and j == 0: # Top left corner
                if field[y_counter][j + 1][0] == 0:
                    neighbors[3] = True
                if field[y_counter + 1][j + 1][0] == 0:
                    neighbors[4] = True
                if field[y_counter + 1][j][0] == 0:
                    neighbors[5] = True
            elif i == 0 and j == (dim - 1): # Top right corner
                if field[y_counter][j - 1][0] == 0:
                    neighbors[7] = True
                if field[y_counter + 1][j - 1][0] == 0:
                    neighbors[6] = True
                if field[y_counter + 1][j][0] == 0:
                    neighbors[5] = True
            elif i == 0: # Top row minus corners
                if field[y_counter][j - 1][0] == 0:
                    neighbors[7] = True
                if field[y_counter + 1][j - 1][0] == 0:
                    neighbors[6] = True
                if field[y_counter + 1][j][0] == 0:
                    neighbors[5] = True
                if field[y_counter + 1][ j + 1][0] == 0:
                    neighbors[4] = True
                if field[y_counter][j + 1][0] == 0:
                    neighbors[3] = True
            elif i == (dim - 1) and j == 0: # Bottom left corner
                if field[y_counter - 1][j][0] == 0:
                    neighbors[1] = True
                if field[y_counter - 1][j + 1][0] == 0:
                    neighbors[2] = True
                if field[y_counter][j + 1][0] == 0:
                    neighbors[3] = True
            elif i == (dim - 1) and j == (dim - 1): # Bottom right corner
                if field[y_counter][j - 1][0] == 0:
                    neighbors[7] = True
                if field[y_counter - 1][j - 1][0] == 0:
                    neighbors[0] = True
                if field[y_counter - 1][j][0] == 0:
                    neighbors[1] = True
            elif i == (dim - 1): # Bottom row minus corners
                if field[y_counter][j - 1][0] == 0:
                    neighbors[7] = True
                if field[y_counter - 1][j - 1][0] == 0:
                    neighbors[0] = True
                if field[y_counter - 1][j][0] == 0:
                    neighbors[1] = True
                if field[y_counter - 1][j + 1][0] == 0:
                    neighbors[2] = True
                if field[y_counter][j + 1][0] == 0:
                    neighbors[3] = True            
            elif j == 0: # Left column minus corners
                if field[y_counter - 1][j][0] == 0:
                    neighbors[1] = True
                if field[y_counter - 1][j + 1][0] == 0:
                    neighbors[2] = True
                if field[y_counter][j + 1][0] == 0:
                    neighbors[3] = True
                if field[y_counter + 1][j + 1][0] == 0:
                    neighbors[4] = True
                if field[y_counter + 1][j][0] == 0:
                        neighbors[5] = True
            elif j == (dim - 1): # Right column minus corners
                if field[y_counter - 1][j][0] == 0:
                    neighbors[1] = True
                if field[y_counter - 1][j - 1][0] == 0:
                    neighbors[0] = True
                if field[y_counter][j - 1][0] == 0:
                    neighbors[7] = True
                if field[y_counter + 1][j - 1][0] == 0:
                    neighbors[6] = True
                if field[y_counter + 1][j][0] == 0:
                    neighbors[5] = True
            else: # All middle squares
                if field[y_counter][j - 1][0] == 0:
                    neighbors[7] = True
                if field[y_counter - 1][j - 1][0] == 0:
                    neighbors[0] = True
                if field[y_counter - 1][j][0] == 0:
                    neighbors[1] = True
                if field[y_counter - 1][j + 1][0] == 0:
                    neighbors[2] = True
                if field[y_counter][j + 1][0] == 0:
                    neighbors[3] = True
                if field[y_counter + 1][j + 1][0] == 0:
                    neighbors[4] = True
                if field[y_counter + 1][j][0] == 0:
                    neighbors[5] = True
                if field[y_counter + 1][j - 1][0] == 0:
                    neighbors[6] = True
            if True in neighbors:
            # Counting up how many neighbors are mined
                for item in neighbors:
                    if item == True:
                        square_sum += 1
                field[y_counter][j][0] = square_sum
            j += 1
        i += 1

def print_current_field():
    display_field = "     "
    for i in range(dim): # Header row
        if i == (dim - 1):
            display_field = display_field + " " + str(i + 1)
        else:
            display_field = display_field + " " + str(i + 1) + " -"
    display_field = display_field + "\n"
    for j in range(dim): # Left coord column
        if j == 9:
            display_field = display_field + str(j + 1) + ": |"
        else:
            display_field = display_field + str(j + 1) + ":  |"
        for k in range(dim): # Main body
            if field[k][j][1] == 0:
                display_field = display_field + " X |"
            elif field[k][j][0] == -1 and field[k][j][1] == 1:
                display_field = display_field + " - |"
            elif field[k][j][0] == 0 and field[k][j][1] == 1:
                display_field = display_field + " * |"
            else:
                display_field = display_field + " " + str(field[k][j][0]) + " |"
        display_field = display_field + "\n"
    return display_field

def kaboomer():
# Mushroom cloud graphic
# Found on asciiart.eu
    boomer ="      _ ._  _ , _ ._ \n" + \
            "    (_ ' ( `  )_  .__) \n" + \
            "  ( (  (    )   `)  ) _) \n" + \
            " (__ (_   (_ . _) _) ,__) \n" + \
            "     `~~`\ ' . /`~~` \n" + \
            "          ;   ; \n" + \
            "          /   \ \n" + \
            "    _____/_ __ \_____    \n" + \
            "        KABOOM!!!          "

    return boomer

def reveal_field():
# Turns entire field visible
    global field
    for i in range(dim):
        for j in range(dim):
            field[i][j][1] = 1
    return

def contiguous(y,x):
# Turn all contiguous non-mined squares visible
    global field
    if field[y][x][1] == 1:
        return
    else:
        reveal_square(y,x)
    limits = list(range(0, dim))
    if (x - 1) in limits and \
    field[y][x - 1][0] == -1 and \
    field[y][x - 1][1] == 0: # x - 1
        contiguous(y,x - 1)
    if (x - 1) in limits and \
    (y - 1) in limits and \
    field[y][x - 1][0] == -1 and \
    field[y][x - 1][1] == 0: # x - 1, y - 1
        contiguous(y - 1,x - 1)
    if (y - 1) in limits and \
    field[y - 1][x][0] == -1 and \
    field[y - 1][x][1] == 0: # y - 1
        contiguous(y - 1, x)
    if (x + 1) in limits and \
    (y - 1) in limits and \
    field[y - 1][x + 1][0] == -1 and \
    field[y - 1][x + 1][1] == 0: #
        contiguous(y - 1,x + 1)
    if (x + 1) in limits and \
    field[y][x + 1][0] == -1 and \
    field[y][x + 1][1] == 0:
        contiguous(y,x + 1)
    if (x + 1) in limits and \
    (y + 1) in limits and \
    field[y + 1][x + 1][0] == -1 and \
    field[y + 1][x + 1][1] == 0:
        contiguous(y + 1,x + 1)
    if (y + 1) in limits and \
    field[y + 1][x][0] == -1 and \
    field[y + 1][x][1] == 0:
        contiguous(y + 1, x)
    if (x - 1) in limits and \
    (y + 1) in limits and \
    field[y + 1][x - 1][0] == -1 and \
    field[y + 1][x - 1][1] == 0:
        contiguous(y + 1, x - 1)
    return

def reveal_square(y,x):
# Marks square as visible
    global field
    field[y][x][1] = 1
    return

def winner(remaining):
    global mine_loc
    winner = False
    if remaining == mine_loc:
        winner = True
    else:
        winner = False
    return winner

def champion():
# Ascii art for winner
# Found on asciiart.eu
# Created by Joan G Stark
    champ =" _______________ \n" \
           "|@@@@|     |####| \n" \
           "|@@@@|     |####| \n" \
           "|@@@@|     |####| \n" \
           "\@@@@|     |####/ \n" \
           " \@@@|     |###/  \n" \
           "  `@@|_____|##'   \n" \
           "       (O)        \n" \
           "    .-'''''-.     \n" \
           "  .'  * * *  `.   \n" \
           " :  *       *  :  \n" \
           ": ~ C H A M P ~ : \n" \
           ": ~ --------- ~ : \n" \
           " :  *       *  :  \n" \
           "  `.  * * *  .'   \n" \
           "    `-.....-'     \n" 
    return champ

def play_game():
    global field
    global mine_loc
    current_guess = ()
    kaboom = False
    win = False
    setup()
    mine_setup()
    start_field()
    aligner()
    print(print_current_field())
    while win == False and kaboom == False:
        current_guess = guess()
        if current_guess == (-1):
            print("Your guess coordinates must be 1 - " + str(dim) + ", try again.")
            continue
        else:
            print("Your guess was: " + str(current_guess[0] + 1) + "," + str(current_guess[1] + 1) + "\n")
            if field[current_guess[1]][current_guess[0]][0] == 0:
                kaboom = True
                print(kaboomer())
                reveal_field()
                print(print_current_field())
            elif field[current_guess[1]][current_guess[0]][0] == -1:
                contiguous(current_guess[1],current_guess[0])
                print(print_current_field())
            else:
                reveal_square(current_guess[1],current_guess[0])
                print(print_current_field())
            # Start work here, trying to figure out how to determine the win
            remaining = []
            for i in range(dim):
                for j in range(dim):
                    if field[i][j][1] == 0:
                        remaining.append([(j + 1), (i + 1)])
            win = winner(remaining)
    if win == True:
        print(champion())
        print("YOU WIN!")
    if kaboom == True:
        print("YOU LOSE!")