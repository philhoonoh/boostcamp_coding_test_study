import sys
import heapq

def is_valid(x, y, n):
    if -1 < x < n and -1 < y < n:
        return True
    return False

t = int(input())

INF = int(1e9)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    graph = []
    for i in range(n):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

    distance = [[INF] * (n) for j in range(n)]

    q = []
    x, y = 0, 0
    dist = graph[0][0]
    heapq.heappush(q, (dist, x, y))
    distance[x][y] = dist


    while q:
        dist, cur_x, cur_y = heapq.heappop(q)

        if distance[cur_x][cur_y] < dist:
            continue

        for delta_x, delta_y in zip(dx, dy):
            next_x, next_y = cur_x + delta_x, cur_y + delta_y
            if not is_valid(next_x, next_y, n):
                continue

            cost = dist + graph[next_x][next_y]
            if cost < distance[next_x][next_y]:
                distance[next_x][next_y] = cost
                heapq.heappush(q, (cost, next_x, next_y))

    print(distance[n-1][n-1])


