# https://www.acmicpc.net/problem/15686

from itertools import combinations

N, M = map(int, input().split())
array = []
for i in range(N):
    array.append([int(k) for k in input().split()])

house_lst = []
chicken = []

for i in range(N):
    for j in range(N):
        if array[i][j] == 1:
            house_lst.append([i+1, j+1])
        if array[i][j] == 2:
            chicken.append([i+1,j+1])

chicken_cand_lst = list(combinations(chicken, M))

def cal_dist(house, chicken):
    dist = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
    return dist

def cal_min(house_lst, chicken_cand):
    total_dist = 0
    for house in house_lst:
        dist = []
        for chicken in chicken_cand:
            dist_ = cal_dist(house, chicken)
            dist.append(dist_)
        total_dist += min(dist)
    return total_dist

dist_lst = []
for chicken_cand in chicken_cand_lst:
    cur_dist = cal_min(house_lst, chicken_cand)
    dist_lst.append(cur_dist)

print(min(dist_lst))
