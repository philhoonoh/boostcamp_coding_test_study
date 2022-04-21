# https://www.acmicpc.net/problem/3190

from collections import deque

n = int(input())
k = int(input())
apple_lst = []
for i in range(k):
    apple_lst.append([int(k) for k in input().split()])
l = int(input())
d_lst = []
for i in range(l):
    s, c = input().split(' ')
    d_lst.append([int(s), c])

d_lst = deque(d_lst)

board = [[0] * n for _ in range(n)]

for x, y in apple_lst:
    board[x-1][y-1] = 1

class Snake():
    def __init__(self):
        self.pos = deque([[0, 0]])
        self.direction = 0

cnt = 0
direction = 0
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

snake = Snake()

def check_valid(next_x, next_y, n, snake):
    if 0 <= next_x < n and 0 <= next_y < n and [next_x, next_y] not in snake.pos:
        return True
    return False

cnt = 0

while True:
    if d_lst:
        if cnt == d_lst[0][0]:
            _, dir = d_lst.popleft()
            if dir == 'L':
                snake.direction = (snake.direction + 1) % 4
            if dir == 'D':
                snake.direction = (snake.direction - 1) % 4

    next_x, next_y = snake.pos[-1][0] + dx[snake.direction], snake.pos[-1][1] + dy[snake.direction]
    if not check_valid(next_x, next_y, n, snake):
        cnt += 1
        break

    if board[next_x][next_y] == 1:
        board[next_x][next_y] = 0
        snake.pos.append([next_x, next_y])
    else:
        snake.pos.append([next_x, next_y])
        snake.pos.popleft()
    cnt += 1

print(cnt)

