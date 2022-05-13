# 벽 부수고 이동하기

from collections import deque
from copy import deepcopy
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()
queue.append([0, 0])

answers = []

def break_wall(cnt):
    if cnt == 1:
        copy_graph = deepcopy(graph)
        bfs(copy_graph)
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                graph[i][j] = 0
                break_wall(cnt + 1)
                graph[i][j] = 1


def bfs(graph):
    global answer

    cnt_graph = [[0] * m for _ in range(n)]
    cnt_graph[0][0] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0 and cnt_graph[nx][ny] == 0:
                cnt_graph[nx][ny] = cnt_graph[x][y] + 1
                queue.append([nx, ny])
    
    if cnt_graph[n - 1][m - 1] != 0:
        answers.append(cnt_graph[n - 1][m - 1])

break_wall(0)

answer = min(answers) if len(answers) >= 1 else -1
print(answer)