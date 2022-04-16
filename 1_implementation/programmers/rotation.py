def rotate_matrix(grid):
    return list(map(list, zip(*reversed(grid))))

def print_matrix(grid):
    for row in grid:
        print(row)
        print('----')

grid = [['1', '2'],
        ['.', '0']]

# check original matrix
print_matrix(grid)

# reverse the outer list
print_matrix(list(reversed(grid)))

# zip the reversed list
print_matrix(rotate_matrix(grid))