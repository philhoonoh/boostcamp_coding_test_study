n = int(input())
m = int(input())

INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    start_, end_, cost = map(int, input().split())
    if cost < graph[start_][end_]:
        graph[start_][end_] = cost

def floyd(n, graph):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    return graph

result = floyd(n, graph)
for i in range(1, n+1):
    for j in range(1, n+1):
        if result[i][j] != INF:
            print(result[i][j], end = ' ')
        else:
            print('0', end=' ')
    print()