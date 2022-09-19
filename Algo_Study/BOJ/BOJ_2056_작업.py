from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
indegree = [0] * (N + 1)
values = [0] * (N + 1)

# dp[K] -> K번 쨰 수를 제거할 때 최소 작업 시간
dp = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    value, edge_cnt, *edge_list = map(int, input().split())
    values[i] = value
    indegree[i] = edge_cnt
    
    for end in edge_list:
        graph[end].append(i)

q = deque()

temp = 0
for i in range(1, N + 1):
    if indegree[i] == 0:
        temp = max(temp, values[i])
        q.append(i)
        dp[i] = values[i]

while q:
    current = q.popleft()

    for i in graph[current]:
        indegree[i] -= 1
        dp[i] = max(dp[i], dp[current] + values[i])

        if indegree[i] == 0:
            q.append(i)

print(dp[N])