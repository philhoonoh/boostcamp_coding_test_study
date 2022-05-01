# https://www.acmicpc.net/problem/18310

n = int(input())
house_lst = list(map(int, input().split()))
house_lst.sort()
# print(house_lst)
total_dist = sum([i - house_lst[0] for i in house_lst])

# index 를 옮겨 가며 계산
distance_lst = [total_dist]

# right index i
for i in range(1, n):
    right_houses = n - i
    left_houses = i
    total_dist -= (house_lst[i] - house_lst[i-1]) * right_houses
    total_dist += (house_lst[i] - house_lst[i-1]) * left_houses
    distance_lst.append(total_dist)

print(house_lst[distance_lst.index(min(distance_lst))])