import sys

n = int(sys.stdin.readline().rstrip())

# 못생긴 수 배열
ugly = [0] * n
ugly[0] = 1

# 2배, 3배, 5배를 이용한 index
# 각각 못생긴 수들의 생성시 사용
i2 = i3 = i5 = 0

# 처음 곱셈 초기화
# 다음 차례의 못생긴 수들을 지정
next2, next3, next5 = 2, 3, 5

# 예시)
# 1 다음으로 작은 못생긴 수 (2,3,5) 선택 -> 2
# 1, 2 다음으로 못생긴 수 2의 배수 생성 // 이때 i2 사용-> 4
# 1, 2 다음으로 못생긴 수 선택 (4,3,5) -> 3
# 1, 2, 3 다음으로 못생긴 3의 배수의 생성 // 이때 i3 사용 -> 6
# 1, 2, 3 다음으로 못생긴 수 선택 (4,6,5) -> 4
# 1, 2, 3, 4 다음으로 못생긴 2의 배수 생성 // 이때 i2  사용 -> 6
# 1, 2, 3, 4 다음으로 못생긴 수 (6,6,5) 선택 -> 5
# 1, 2, 3, 4, 5 다음으로 못생긴 5의 배수 생성 // 이때 i5  사용 -> 10
# 1, 2, 3, 4, 5 다음으로 못생긴 수 (6,6,10) 선택 -> 6
# 1, 2, 3, 4, 5, 6 다음으로 못생긴 2,3의 배수 생성 // 이때 i2, i3 동시 사용 -> 8, 9
# 1, 2, 3, 4, 5, 6 다음으로 못생긴 수 (8, 9, 10) 선택 -> 8
# ....

for l in range(1, n):

    ugly[l] = min(next2, next3, next5)

    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[n-1])