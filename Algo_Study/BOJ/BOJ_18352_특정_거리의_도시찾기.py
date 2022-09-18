from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())


graph = [list() for _ in range(N + 1)]
count = [0 for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
answers = set()


queue = deque([X])
count[X] = 0

for i in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)

while queue:
    v = queue.popleft()
    visited[v] = True
    
    for next in graph[v]:
        if not visited[next]:
            visited[next] = True
            queue.append(next)
            count[next] = count[v] + 1

            if count[next] == K:
                answers.add(next)

answers = list(answers)
answers.sort()

if len(answers) == 0:
    print(-1)
else :
    for answer in answers:
        print(answer)