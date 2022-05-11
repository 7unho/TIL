# 연구소
## N * M의 크기의 연구소는 빈 칸(0)과 벽(1)으로 이루어져 있다.
## 바이러스(2)는 상하좌우 인접한 빈 칸으로 퍼져 나간다.
## 새로 세울 수 있는 벽의 개수는 무조건 3개이다.
## 벽을 3개 세웠을 때 안전 영역의 최댓값을 구하라

from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
answer = 0



dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def start_virus():
    global answer
    zero_cnt = 0
    
    copy_graph = deepcopy(graph)

    for i in range(n):
        for j in range(m):
            if copy_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if copy_graph[nx][ny] == 0:
                copy_graph[nx][ny] = 2
                queue.append((nx, ny))
    
    for i in range(n):
        zero_cnt += copy_graph[i].count(0)

    answer = max(answer, zero_cnt)

def make_wall(x):
    if x == 3:
        start_virus()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(x + 1)
                graph[i][j] = 0

make_wall(0)
print(answer)
