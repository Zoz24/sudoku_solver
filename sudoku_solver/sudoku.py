# This function checks for an empty spot in the grid that hasn't been filled up yet
def search_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == -1:
                return i, j
    return None# Return none if all spots have been filled up 

# This function print out the sudoku grid
def print_grid(grid):
    for i in range(len(grid)):
        if i != 0 and i % 3 == 0: # Seperate each vertical stack
            print('--------------------')
        for j in range(len(grid[0])):
            if j != 0 and j % 3 == 0: # Seperate each block
                print('|', end='') 
            print(grid[i][j], end = ' ')
        print()

def validation(num, row, col, grid):
    # Check if the input number contracdicts with any number in the row
    if num in grid[row]:
        return False
    # Check if the input number contradicts with any number in the column
    for i in range(len(grid)):
        if num == grid[i][col]:
            return False

    # Check if the input number contracts with any number within its block
    start_row = row // 3 * 3
    start_col = col // 3 * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    # Return True if no contradiction was found
    return True

# Uses recursion and backtracking to solve the Sudoku grid
def solver(grid):
    # Base case: 
    if search_empty(grid) == None:
        return True
    else:
        row, col = search_empty(grid)
    
    for i in range(1, 10):
        if validation(i, row, col, grid):
            grid[row][col] = i
            if solver(grid):
                return True
        grid[row][col] = -1
    
    return False

def main():
    # Creating a grid for testing purpose, can change into different grid if necessary
    test_grid = [
        [4, -1, -1,   -1, -1, -1,   9, -1, -1],
        [-1, -1, -1,   -1, 3, -1,   -1, -1, -1],
        [-1, 1, -1,   -1, 6, 5,   -1, 4, -1],

        [-1, -1, -1,   3, -1, -1,   -1, 5, -1],
        [-1, -1, 6,   -1, 5, 2,   7, -1, -1],
        [-1, 2, -1,   9, -1, -1,   -1, -1, -1],

        [-1, -1, -1,   2, -1, -1,   -1, -1, -1],
        [-1, 6, -1,   -1, 4, 1,   -1, 9, -1],
        [-1, -1, 7,   -1, -1, -1,   -1, -1, 8]
    ]

    if (solver(test_grid)):
        print("The solution is found and is shown below:")
        print_grid(test_grid)
    else:
        print("The Sudoku grid is not solvable, check for errors")

if __name__ == '__main__':
    main()