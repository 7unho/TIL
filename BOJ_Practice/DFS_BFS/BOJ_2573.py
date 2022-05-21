# 빙산

## 빙산 덩어리 체크용 dfs 함수
def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if dfs_graph[x][y] > 0:
        dfs_graph[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            dfs(nx, ny)
        return True
    return False

from copy import deepcopy
import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = 0

for _ in range(max(n, m)):
    dfs_graph = deepcopy(graph)
    ice_grp = 0

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if dfs(i, j):
                ice_grp += 1
    
    if ice_grp >= 2:
        break

    answer += 1
    
print(answer if ice_grp > 2 else 0)
