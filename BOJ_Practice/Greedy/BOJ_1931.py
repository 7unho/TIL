# 회의실 배정 remind

import sys
input = sys.stdin.readline

n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]
array.sort(key=lambda x : (x[1], x[0]))

answer = 1
temp = array[0]

for i in range(1, len(array)):
    if array[i][0] >= temp[1]:
        answer += 1
        temp = array[i]
        continue

print(answer)