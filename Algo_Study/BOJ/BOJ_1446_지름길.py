# 입력값 : 지름길 (N), 도로의 길이 (D)
import heapq
import sys
input = sys.stdin.readline

N, D = map(int, input().split())
graph = [[(i + 1, 1)] for i in range(D)]
graph.append([])
dp = [10_001] * (D + 1)

for _ in range(1, N + 1):
    start, end, dist = map(int, input().split())
    if end > D :
        continue
    graph[start].append((end, dist))


def solution(start):
    queue = list()
    heapq.heappush(queue, (start, 0))
    dp[0] = 0

    while queue:
        current, dist = heapq.heappop(queue)

        if dp[current] < dist:
            continue

        for next in graph[current]:
            cost = dist + next[1]

            if cost < dp[next[0]]:
                dp[next[0]] = cost
                heapq.heappush(queue, (next[0], cost))

solution(0)

print(dp[D])