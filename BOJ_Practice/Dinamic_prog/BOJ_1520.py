# 내리막길
## 인접한 노드 중 현재 노드보다 작은 값을 갖는 노드로만 이동할 때,
## 도착지까지의 경우의 수

def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if not visited[x][y]:
        visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[x][y] > graph[nx][ny]:
                dfs(nx, ny)
                return True
    return False

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
answer = 0

if dfs(0, 0):
    answer += 1

print(answer)
print(visited)