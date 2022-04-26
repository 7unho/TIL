# 보석 도둑

## 입력값 : N(보석의 개수), K(가방의 개수)
##        각 보석의 정보(무게 : M, 가격 : V)
##        각 가방의 정보(무게 : C)

import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())

jewels = []

for _ in range(n):
    m, v = map(int, input().split())
    jewels.append((-v, m))

heapq.heapify(jewels)
bags = [int(input()) for _ in range(k)]
bags.sort()
answer = 0
jew_temp = []

for i in range(k):
    while True:
        if not jewels:
            break

        temp = heapq.heappop(jewels)
        
        if bags[i] >= temp[1]:
            answer -= temp[0]
            break
        
        jew_temp.append(temp)
    
    for jew in jew_temp:
        heapq.heappush(jewels, (jew[0], jew[1]))

print(answer)