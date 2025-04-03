def show_instructions():
    '''Print game rules.

    Print starting objects position.
    '''
    print(('===== CONTROLS =====: \n'), ('Input "Start" to begin \n'), ('Input Object \n'),
          ('Input Direction \n'), ('Default Objects Placement:'))
    

# Defaults and Controls
pos = [['Table', 'Chair', 'Wardrobe'], ['Chair_2', 'Empty', 'Armchair']]
mov = ["Up", "Left", "Down", "Right"]

# Object to symbol mapping for visualization
symbol_map = {
    "Empty": "[          ]",
    "Wardrobe": "[ Wardrobe ]",
    "Table": "[   Table  ]",
    "Chair": "[   Chair  ]",
    "Chair_2": "[  Chair_2 ]",
    "Armchair": "[ Armchair ]"
}


def display_board():
    '''Visualize current object placements on the board.
    '''
    print('=' * 38)
    for row in pos:  # Iterates over rows directly
        row_visual = [symbol_map[obj] for obj in row]
        print(*row_visual)
    print('=' * 38)


def move(item, direction):
    '''Move items within the grid.
    '''
    for i in range(len(pos)):  # Dynamically retrieve number of rows
        for j in range(len(pos[i])):  # Dynamically retrieve number of columns
            if pos[i][j] == item:
                row, col = i, j
                break
        else:
            continue
        break
    else:
        print("Object not found")
        return  # Added return to exit function

    # Move object based on direction input
    if direction == "Left" and col > 0 and pos[row][col - 1] == "Empty":
        pos[row][col - 1], pos[row][col] = pos[row][col], pos[row][col - 1]
    elif direction == "Right" and col < len(pos[row]) - 1 and pos[row][col + 1] == "Empty":
        pos[row][col + 1], pos[row][col] = pos[row][col], pos[row][col + 1]
    elif direction == "Up" and row > 0 and pos[row - 1][col] == "Empty":
        pos[row - 1][col], pos[row][col] = pos[row][col], pos[row - 1][col]
    elif direction == "Down" and row < len(pos) - 1 and pos[row + 1][col] == "Empty":
        pos[row + 1][col], pos[row][col] = pos[row][col], pos[row + 1][col]
    else:
        print("Can't be moved here")

# Main game loop
show_instructions()
display_board()
if input("Type 'Start' to begin: ") == "Start":
    while True:
        item = input("Enter item to move: ")
        direction = input("Enter direction (Up, Down, Left, Right): ")
        move(item, direction)
        display_board()

        # Check if the game is completed
        if pos[0][2] == "Armchair" and pos[1][2] == "Wardrobe":
            print('Good job!')
            break