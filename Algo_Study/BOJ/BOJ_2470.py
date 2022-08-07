# 두 용액
## 입력 값 : 용액의 수 (N)[2 ~ 100,000] 출력값 : 0에 가장 가까운 두 수의 오름차순
import sys
input = sys.stdin.readline

N = int(input())

array = list(map(int, input().split()))
array.sort()

start = 0
end = N - 1

condition = 2_000_000_001
answer = []

while True:
    if start >= end:
        break

    current = array[start] + array[end]

    print(condition, current)
    if condition > abs(current):
        condition = abs(current)
        answer = [array[start], array[end]]

    if current < 0:
        start += 1
    else:
        end -= 1    

print(answer[0], answer[1])
