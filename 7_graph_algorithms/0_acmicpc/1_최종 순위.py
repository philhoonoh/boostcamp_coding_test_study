from collections import deque

def solution():
    n = int(input())
    previous = list(map(int, input().split()))

    graph = [[] for i in range(n+1)]
    indegree = [0] * (n+1)

    for i in range(0, n):
        cur_team = previous[i]
        indegree[cur_team] = i
        for j in range(i+1, n):
            graph[previous[i]].append(previous[j])


    m = int(input())
    for j in range(m):
        up, down = map(int, input().split())
        if up in graph[down]:
            graph[up].append(down)
            graph[down].remove(up)
            indegree[down] += 1
            indegree[up] -= 1
        elif down in graph[up]:
            graph[down].append(up)
            graph[up].remove(down)
            indegree[down] -= 1
            indegree[up] += 1

    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    if len(q) > 1:
        return 'IMPOSSIBLE'

    # print('----')
    # for row in graph:
    #     print(row)
    # print('----')
    #
    # print(f'indegree : {indegree}')

    result = []
    while q:
        # print(f'each q : {q}')
        cur = q.popleft()
        result.append(cur)

        cnt = 0
        for next in graph[cur]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
                cnt += 1
            if cnt > 1:
                return '?'
        # print(f'indegree : {indegree}')

    # print(f'result : {result}')
    if len(result) == n:
        return ' '.join([str(i) for i in result])
    else:
        return 'IMPOSSIBLE'

t = int(input())
for _ in range(t):
    print(solution())