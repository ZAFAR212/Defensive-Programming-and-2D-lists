# Request user to input a grid: 
grid = [ ["-", "-", "-", "#", "#"],
       ["-", "#", "-", "-", "-"],
       ["-", "-", "#", "-", "-"],
       ["-", "#", "#", "-", "-"],
       ["-", "-", "-", "-", "-"] ]

# define a function called bomb counter
def grid_bomb_counter(grid_input):
    # assign the user input grid to a variable
    grid = grid_input
    # iterate through rows and columns of the grid
    for row_index, row in enumerate(grid):
        for col_index,col in enumerate(row):
            # for every cell, create/restart the bomb counter
            bomb_counter = 0
            # only perform the logic below if the value is a dash as we dont care about # adjacent to #
            if col == "-":
                # Apply positional index logic prefaced by the boolean to ensure values are not out of range
             # North West
                if  (0 <= row_index-1 <= len(grid)-1) and  (0 <= col_index-1 <= len(row)-1) and (grid[row_index-1][col_index-1] == "#"):
                    bomb_counter += 1
            # North
                if  (0 <= row_index-1 <= len(grid)-1) and  (0 <= col_index   <= len(row)-1) and (grid[row_index-1][col_index] == "#"):
                    bomb_counter += 1
            # North East
                if  (0 <= row_index-1 <= len(grid)-1) and  (0 <= col_index+1 <= len(row)-1) and (grid[row_index-1][col_index+1] == "#"):
                    bomb_counter += 1
            # West
                if  (0 <= row_index   <= len(grid)-1) and  (0 <= col_index-1 <= len(row)-1) and (grid[row_index][col_index-1] == "#"):
                    bomb_counter += 1
            # East
                if  (0 <= row_index   <= len(grid)-1) and  (0 <= col_index+1 <= len(row)-1) and (grid[row_index][col_index+1] == "#"):
                    bomb_counter += 1
            # South West
                if  (0 <= row_index+1 <= len(grid)-1) and  (0 <= col_index-1 <= len(row)-1) and (grid[row_index+1][col_index-1] == "#"):
                    bomb_counter += 1
            # South
                if  (0 <= row_index+1 <= len(grid)-1) and  (0 <= col_index   <= len(row)-1) and (grid[row_index+1][col_index] == "#"):
                    bomb_counter += 1
            # South East
                if  (0 <= row_index+1 <= len(grid)-1) and  (0 <= col_index+1 <= len(row)-1) and (grid[row_index+1][col_index+1] == "#"):
                    bomb_counter += 1
            # replace the mine free spot with the bomb counter
                grid[row_index][col_index] = bomb_counter
            else:
            # if the cell value is # then keep it as #
                grid[row_index][col_index] = "#"
    # return the output
    return grid

# call the function        
output_grid = grid_bomb_counter(grid_input = grid)
# cosmetically enhance the output to look like what was requested in the pdf
print('\n'.join(map(str,output_grid)))


