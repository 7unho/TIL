import sys
input = sys.stdin.readline

N = int(input())
array = []

for _ in range(N):
    start, end = map(int, input().split())
    array.append([start, end])

array.sort(key=lambda x : (x[1], x[0]))

last = 0
answer = 0

for start, end in array:
    if start >= last:
        answer += 1
        last = end
    
print(answer)