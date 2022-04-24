# 내리막길
## 인접한 노드 중 현재 노드보다 작은 값을 갖는 노드로만 이동할 때,
## 도착지까지의 경우의 수

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    graph[i].insert(0, 0)
graph.insert(0, [0 for _ in range(m + 1)])

d = [[0] * (m + 1) for _ in range(n + 1)]

