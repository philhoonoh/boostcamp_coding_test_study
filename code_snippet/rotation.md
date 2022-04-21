# matrix rotation
- 알고리즘 문제를 풀다 보면 matrix를 rotation 해야될때가 많다.
- 여러가지 방법이 있지만 가장 zip과 unpacking을 활용한 pythonic한 방법
- matrix가 MxN 일때도 가능한 코드

```python

def rotate_matrix(grid):
    return list(map(list, zip(*reversed(grid))))

def print_matrix(grid):
    for row in grid:
        print(row)

# matrix 
grid = [['1', '2'],
        ['.', '0']]

# check original matrix
print_matrix(grid)
# ['1', '2']
# ['.', '0']

# reverse the outer list
print_matrix(list(reversed(grid)))
# ['.', '0']
# ['1', '2']

# zip the reversed list
print_matrix(rotate_matrix(grid))
# ['.', '1']
# ['0', '2']

```




