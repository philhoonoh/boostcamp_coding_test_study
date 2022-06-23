import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))

def binary_search(arr):
    lower = 0
    upper = len(arr) - 1

    while lower <= upper:
        mid = (lower + upper) // 2
        # print(f'arr : {arr}')
        # print(f'upper : {upper}')
        # print(f'mid : {mid}')
        # print(f'lower : {lower}')
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            lower = mid + 1
        elif arr[mid] > mid:
            upper = mid - 1
    return -1

print(binary_search(arr))