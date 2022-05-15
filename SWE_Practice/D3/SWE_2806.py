# N-Queen
import sys
n = int(input())

graph = [[0] * n for _ in range(n)]
answer = 0

dx = [1, 1, -1, -1]
dy = [-1, 1, 1, -1]


def check_queen(x, y):

    # 가로 체크
    if graph[x].count(1) != 0:
        return False

    # 세로 체크
    for i in range(n):
        if graph[i][y] == 1:
            return False
    
    # 대각선 체크...
        



def make_queen(cnt):
    global answer 

    if cnt == n:
        return True
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0 and check_queen(i, j):
                graph[i][j] = 1
                make_queen(cnt + 1)
                graph[i][j] = 0
                answer += 1

make_queen(0)
print(answer)




