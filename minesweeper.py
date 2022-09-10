import random
mine_loc = []
field = []
dim = 10
mines = 10

# TO DO Items
#   - Determine field dimensions -- done
#   - Determine number of mines -- done
#   - Pick unique mine locations within field -- done
#   - Prompt user for coordinates of picks
#   - Create list "array" of field -- done
#   - Add notation for area within 1 square of mines -- done
#   - Determine status of mines
#   - Determine what is within an 3x3 grid of whichever place is selected
#       - Reveal all mines if cell is mined
#       - Highlight cell with number if it's next to 1 or more mines
#       - Clear cell and all adjacent non-mined cells if it's not next to a mine
#   - Update TO DO list

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
    gx = int(input("What is your next guess X-axis component?: ")) - 1
    # Receive input on x component
    if gx < 0 or gx == (dim):
    # Validate x component is within constraints
        gx_ready = False
    else:
        gx_ready = True
    gy = int(input("What is your next guess Y-axis component?: ")) - 1
    # Receive input on y component
    if gy < 0 or gy == (dim):
    # Validate y component is within constraints
        gy_ready = False
    else:
        gy_ready = True
    if gx_ready == True and gy_ready == True:
    # If x/y components within constraints, return (x, y) tuple
        return (gx, gy)
    else:
    # If x/y components not within constraints, recurse to try again
        guess()

def start_field():
# Creates field to track mines, squares, and guesses
    global field
    # Tracks status of field and mines
    mine_symbol = 0
    # Annotates mine on field
    field = [[-1] * (len(range(dim))) for i in range(dim)]
    # Creates field with [[dim]dim] nested list
    counter = 0
    while counter != (mines):
        field[int(mine_loc[counter][1]) - 1][int(mine_loc[counter][0]) - 1] = mine_symbol
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
            if field[y_counter][j] == 0:
            # Ignores square if mined
                neighbors[0] = False
            elif i == 0 and j == 0: # Top left corner
                if field[y_counter][j + 1] == 0:
                    neighbors[3] = True
                if field[y_counter + 1][j + 1] == 0:
                    neighbors[4] = True
                if field[y_counter + 1][j] == 0:
                    neighbors[5] = True
            elif i == 0 and j == (dim - 1): # Top right corner
                if field[y_counter][j - 1] == 0:
                    neighbors[7] = True
                if field[y_counter + 1][j - 1] == 0:
                    neighbors[6] = True
                if field[y_counter + 1][j] == 0:
                    neighbors[5] = True
            elif i == 0: # Top row minus corners
                if field[y_counter][j - 1] == 0:
                    neighbors[7] = True
                if field[y_counter + 1][j - 1] == 0:
                    neighbors[6] = True
                if field[y_counter + 1][j] == 0:
                    neighbors[5] = True
                if field[y_counter + 1][ j + 1] == 0:
                    neighbors[4] = True
                if field[y_counter][j + 1] == 0:
                    neighbors[3] = True
            elif i == (dim - 1) and j == 0: # Bottom left corner
                if field[y_counter - 1][j] == 0:
                    neighbors[1] = True
                if field[y_counter - 1][j + 1] == 0:
                    neighbors[2] = True
                if field[y_counter][j + 1] == 0:
                    neighbors[3] = True
            elif i == (dim - 1) and j == (dim - 1): # Bottom right corner
                if field[y_counter][j - 1] == 0:
                    neighbors[7] = True
                if field[y_counter - 1][j - 1] == 0:
                    neighbors[0] = True
                if field[y_counter - 1][j] == 0:
                    neighbors[1] = True
            elif i == (dim - 1): # Bottom row minus corners
                if field[y_counter][j - 1] == 0:
                    neighbors[7] = True
                if field[y_counter - 1][j - 1] == 0:
                    neighbors[0] = True
                if field[y_counter - 1][j] == 0:
                    neighbors[1] = True
                if field[y_counter - 1][j + 1] == 0:
                    neighbors[2] = True
                if field[y_counter][j + 1] == 0:
                    neighbors[3] = True            
            elif j == 0: # Left column minus corners
                if field[y_counter - 1][j] == 0:
                    neighbors[1] = True
                if field[y_counter - 1][j + 1] == 0:
                    neighbors[2] = True
                if field[y_counter][j + 1] == 0:
                    neighbors[3] = True
                if field[y_counter + 1][j + 1] == 0:
                    neighbors[4] = True
                if field[y_counter + 1][j] == 0:
                        neighbors[5] = True
            elif j == (dim - 1): # Right column minus corners
                if field[y_counter - 1][j] == 0:
                    neighbors[1] = True
                if field[y_counter - 1][j - 1] == 0:
                    neighbors[0] = True
                if field[y_counter][j - 1] == 0:
                    neighbors[7] = True
                if field[y_counter + 1][j - 1] == 0:
                    neighbors[6] = True
                if field[y_counter + 1][j] == 0:
                    neighbors[5] = True
            else: # All middle squares
                if field[y_counter][j - 1] == 0:
                    neighbors[7] = True
                if field[y_counter - 1][j - 1] == 0:
                    neighbors[0] = True
                if field[y_counter - 1][j] == 0:
                    neighbors[1] = True
                if field[y_counter - 1][j + 1] == 0:
                    neighbors[2] = True
                if field[y_counter][j + 1] == 0:
                    neighbors[3] = True
                if field[y_counter + 1][j + 1] == 0:
                    neighbors[4] = True
                if field[y_counter + 1][j] == 0:
                    neighbors[5] = True
                if field[y_counter + 1][j - 1] == 0:
                    neighbors[6] = True
            if True in neighbors:
            # Counting up how many neighbors are mined
                for item in neighbors:
                    if item == True:
                        square_sum += 1
                field[y_counter][j] = square_sum
            j += 1
        i += 1


def tester():
    setup()
    mine_setup()
    start_field()
    aligner()
    print(field_pretty())

   
print(tester())
