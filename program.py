def display_grid():
    # creating a grid with predefined letters
    grid = [
        ['A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'H', 'I', 'J'],
        ['K', 'L', 'M', 'N', 'O'],
        ['P', 'Q', 'R', 'S', 'T'],
        ['U', 'V', 'W', 'X', 'Y'],
        ['.' , '.','Z' , '.', '.']
    ]
    # displaing the grid row by row
    for row in grid:
        print(" | ".join(row))
    print()

def get_user_input():
    # looping until the user provides a valid input
    while True:
        try:
            # ask the user for the length of the name
            name_length = int(input("Think of a name. Enter the number of letters (3, 4, or 5): "))
            # check if the input is within the allowed range
            if name_length in [3, 4, 5]:
                break
            else:
                print("Please enter a valid number (3, 4, or 5).")
        except ValueError:
            print("Invalid input. Please enter a number (3, 4, or 5).")
    return name_length

def get_column_indices(name_length, prompt):
    indices = []
    # loop to get the column indices based on the name length
    for i in range(name_length):
        while True:
            try:
                # asking the user for a column index
                index = int(input(f"{prompt} Enter column index {i+1} (1 to 5): "))
                # checking if the index is within the allowed range
                if 1 <= index <= 5:
                    indices.append(index)
                    break
                else:
                    print("Please enter a valid column index (1 to 5).")
            except ValueError:
                print("Invalid input. Please enter a number (1 to 5).")
    return indices

def rearrange_grid(indices):
    # creating the initial grid again
    grid = [
        ['A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'H', 'I', 'J'],
        ['K', 'L', 'M', 'N', 'O'],
        ['P', 'Q', 'R', 'S', 'T'],
        ['U', 'V', 'W', 'X', 'Y'],
        ['.' , '.','Z' , '.', '.']
    ]

    new_grid = []
    # creating a new grid based on the selected columns before
    for index in indices:
        column = index - 1
        new_row = [row[column] for row in grid]
        new_grid.append(new_row)

    print("\nRearranged Grid:")
    # displaying the new grid
    for row in new_grid:
        print(" | ".join(row))
    print()
    return new_grid

def construct_word(grid, indices):
    word = []
    # constructing the word from the new grid based on the final indices
    for i, index in enumerate(indices):
        column = index - 1
        word.append(grid[i][column])
    return ''.join(word)

def main():
    # to display the initial grid
    display_grid()
    # to get the length of the name from the user
    name_length = get_user_input()
    # to get the initial column indices from the user
    initial_indices = get_column_indices(name_length, "Step 1 -")
    # to rearrange the grid based on the initial indices
    rearranged_grid = rearrange_grid(initial_indices)
    # to get the final column indices from the user
    final_indices = get_column_indices(name_length, "Step 2 -")
    # to construct the word from the rearranged grid and final indices
    word = construct_word(rearranged_grid, final_indices)
    # to display the final word
    print(f"\nThe word you thought about is: {word}")


if __name__ == "__main__":
    main()
