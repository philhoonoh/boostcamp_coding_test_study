# https://www.acmicpc.net/problem/14888

n = int(input())
numbers = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

def dfs(n, value, numbers, plus, minus, mul, div):
    if n == 0:
        answer.append(value)

    if plus > 0:
        value_ = value + numbers[0]
        numbers_ = numbers[1:]
        plus_ = plus - 1
        n_ = n - 1
        dfs(n_, value_, numbers_, plus_, minus, mul, div)
    if minus > 0:
        value_ = value - numbers[0]
        numbers_ = numbers[1:]
        minus_ = minus - 1
        n_ = n - 1
        dfs(n_, value_, numbers_, plus, minus_, mul, div)
    if mul > 0:
        value_ = value * numbers[0]
        numbers_ = numbers[1:]
        mul_ = mul - 1
        n_ = n - 1
        dfs(n_, value_, numbers_, plus, minus, mul_, div)
    if div > 0:
        if value < 0 and numbers[0] > 0:
            value_ = abs(value) // numbers[0] * -1
        else:
            value_ = value // numbers[0]
        numbers_ = numbers[1:]
        div_ = div - 1
        n_ = n - 1
        dfs(n_, value_, numbers_, plus, minus, mul, div_)

inital_value = numbers[0]
numbers = numbers[1:]
n -= 1
answer = []
dfs(n, inital_value, numbers, plus, minus, mul, div)
print(max(answer))
print(min(answer))
