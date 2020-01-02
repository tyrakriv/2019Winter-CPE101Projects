# PROJECT 4
#
# Name: Tyra Krivonak and Shriya Nimmagadda
# S. Einakian

def main():
    pass

# Initialize temp and col lists
# Create a for loop to go through each index of range 5
# Create a second for loop to go through each item within the index
# Append every item into col list

# This function will go through the entire input grid and return a columns 2D list
# list -> list
def transpose(grid):
    col = []
    temp = []
    for i in range(5):
        for j in range(5):
            temp.append(grid[j][i])
        col.append(temp[i*5:i*5+5])
    return col

# Call validate_row, validate_cols, validate_cages to determine booleans
# Determine if every function returns True or False
# If every function called returns True, return True
# If not, return False

# This function will call functions to determine if all columns, rows, and cages are valid and return True or False based on input
# list -> boolean
def validate_all(grid, cages):
    row = validate_rows(grid)
    col = validate_cols(grid)
    cag = validate_cages(grid, cages)
    if row == True and col == True and cag == True:
        return True
    else:
        return False

# Initialize all variables: temp and lis
# Create a for loop to go through grid items
# Initialize a count variable to keep track of sum
# Create a second for loop to go through every list in item
# Make temp equal to grid item
# If temp is found in any other item in the list, increment count
# Else, keep looping
# If count is zero at the end, append True to lis
# Else, append False to list
# If false is found anywhere in lis, return False
# Else, return False

# This function will make sure no numbers are duplicated in a row
# list -> boolean
def validate_rows(grid):
    lis = []
    temp = 0
    for i in range(len(grid)):
        cnt = 0
        for j in range(5):
            temp = grid[i][j]
            for k in range(j+1,5):
                if temp == grid[i][k]:
                    cnt += 1
            
        if cnt == 0:
            lis.append(True)
        else:
            lis.append(False)

    if (False) in lis:
        return False
    else:
        return True
  
# Initialize lis and temp variables
# Call transpose function and assign to variable col
# Create a for loop to go through col list
# Initialize count to zero
# Assign temp to col item
# Create a second for loop to determine if temp is duplicated in col list
# If it is, increment count by one
# If not, keep looping
# If count is equal to zero, append True to lis
# If not, append False to lis
# If False is found in lis, return False
# Else, return True

# This function will validate columns and make sure that no duplicates exist
# list -> boolean
def validate_cols(grid):
    lis = []
    temp = 0
    
    col = transpose(grid)

    for i in range(len(col)):
        cnt = 0
        for j in range(5):
            temp = col[i][j]
            for k in range(j+1,5):
                if temp == col[i][k]:
                    cnt += 1
            
        if cnt == 0:
            lis.append(True)
        else:
            lis.append(False)

    if (False) in lis:
        return False
    else:
        return True

# Initialize variables lis and gridoned
# Create a for loop to go through the grid list
# Determine if the type of an item in the grid list is a list
# If it is, create another for loop to append the item within the list to gridoned
# Else, append item to gridoned
# Create a new for loop to go through the second to last item of the cages list
# Set temp to zero and sum to the first item in each cages item
# Create a for loop within to go through each index within every item in cage
# Add integer to temp
# If temp equals the sum, append True to lis
# Else, append False
# At the end, if False is found, return False
# Else, return True

# This function determines if all numbers in a cage adds up to the sum
# list -> boolean
def validate_cages(grid, cages):

    lis = []
    gridoned = []
    
    for i in range(len(grid)):
        if type(grid[i]) == list:
            for x in range (len(grid[i])):
                gridoned.append(grid[i][x])
        else:
            gridoned.append(grid[i])
    
    for i in range(1,cages[0][0]+1):
        temp = 0
        sum = cages[i][0]
        for j in range(1,len(cages[i])):
            
            temp += gridoned[(cages[i][j])]
            
        if temp == sum:
            lis.append(True)
        else:
            lis.append(False)
    
    if (False) in lis:
        return False
    else:
        return True
