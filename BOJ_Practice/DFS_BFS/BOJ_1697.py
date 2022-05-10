# 숨바꼭질
## 입력값 : N (술래의 위치), K (타겟의 위치) 출력값 : 타겟을 찾는 가장 빠른 시간

def make_graph(x):
    graph = [x - 1, x + 1, x * 2]
    return graph

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

queue = deque([n])
visited = []

while queue:
    v = queue.popleft()
    print(v, end=' ')
    if v == k:
        break

    for point in make_graph(v):
        if point <= 0 or point >= 10 ** 6:
            continue

        if point not in visited:
            visited.append(point)
            queue.append(point)

