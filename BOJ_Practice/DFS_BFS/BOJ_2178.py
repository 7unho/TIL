# 미로 탐색

def dfs(x, y):
    if x > n or x <= 0 or y > m or y <= 0:
        return False
    
    if not visited:
        visited[x][y] = True

        dfs(x + 1, y)
        dfs
    pass

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = 0

visited = [[0 for _ in range(m)] for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]

print(visited)