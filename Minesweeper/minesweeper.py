
#Count the number of mines adjacent to a given spot in the grid.
def count_adjacent_mines(grid, row, col):
    mine_count = 0
    rows, cols = len(grid), len(grid[0])

    # Define the eight possible directions to check for adjacent mines
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),(0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    # Iterate through each direction
    for row_offset, col_offset in directions:
        new_row, new_col = row + row_offset, col + col_offset

        # Check if the new position is within the grid bounds
        if 0 <= new_row < rows and 0 <= new_col < cols:
            # Check if there is a mine at the adjacent position
            if grid[new_row][new_col] == '#':
                mine_count += 1

    return mine_count

#Replace each dash in the grid with the number of adjacent mines.
def minesweeper(grid):
    rows, cols = len(grid), len(grid[0])
    
    # Initialize a new grid with the same layout as the original, filled with '0' or original character '#'
    new_grid = []
    for row in grid:
        new_row = []
        for cell in row:
            if cell == '#':
                new_row.append('#')
            else:
                new_row.append('0')
        new_grid.append(new_row)

    # Iterate through each spot in the original grid
    for row in range(rows):
        for col in range(cols):
            # If the current spot is a dash, count the number of adjacent mines
            if grid[row][col] == '-':
                mines_count = count_adjacent_mines(grid, row, col)
                # Update the new grid with the mine count
                new_grid[row][col] = str(mines_count)

    return new_grid

# Testing the functions with an grid example
input_grid = [
    ['#', '-', '#', '-', '#'],
    ['-', '#', '-', '#', '-'],
    ['#', '-', '#', '-', '-'],
    ['-', '#', '-', '#', '-']
]

# Get the result from the Minesweeper function
test_grid = minesweeper(input_grid)

# Print the input and output grids for comparison
print("Input Grid:")
for row in input_grid:
    print(' '.join(row))

print("\nOutput Grid:")
for row in test_grid:
    print(' '.join(row))
