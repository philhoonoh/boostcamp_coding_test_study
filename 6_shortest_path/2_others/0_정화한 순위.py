import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = 1
    # graph[b][a] = 1

def floyd(n, graph):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    return graph

# end 번호로 도착 가능한 번호
def inbound(graph, end):
    idx = []
    for index in range(1, len(result)):
        if 0 < graph[index][end] < INF:
            idx.append(index)
    return idx

# start 번호 에서 갈수 있는 번호
def outbound(graph, start):
    idx = []
    for index, row in enumerate(graph[start]):
        if 0 < row < INF:
            idx.append(index)
    return idx

result = floyd(n, graph)
# for row in result:
#     print(row)
cnt = 0
total_sum = sum([i for i in range(1, n+1)])

for i in range(1, n+1):
    inbound_lst = inbound(result, i)
    outbound_lst = outbound(result, i)
    if sum(inbound_lst + outbound_lst) == total_sum - i:
        cnt += 1
print(cnt)


# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4
# 4번에서 갈수 있는 번호 : 2, 6
# 4번으로 갈수 있는 번호 : 1, 3, 5