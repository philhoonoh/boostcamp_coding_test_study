# 방향바꾸기
- 알고리즘 문제를 풀다 보면 방향을 바꾸어야 될 필요성이 있다
- 현재 방향에서 왼쪽 또는 오른쪽
- 이대 dx, dy 를 설정하고
- direction으로 방향 인덱스를 바꾼다.

```python

# 동, 북, 서, 남
# 0, 1, 2, 3
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 동쪽 
direction = 0
dx[direction] == 1
dy[direction] == 0


# 동쪽에서 북쪽으로 왼쪽으로 방향을 바꾼다
direction += 1
dx[direction] == 0
dy[direction] == 1

# 북쪽에서 서쪽으로 왼쪽으로 방향을 바꾼다
direction += 1
dx[direction] == -1
dy[direction] == 0

# 서쪽에서 북쪽으로 오른쪽으로 방향을 바꾼다
direction -= 1
dx[direction] == 0
dy[direction] == 1

```





