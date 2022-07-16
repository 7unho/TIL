# 숫자 배열 회전

from copy import deepcopy

for tc in range(1, int(input()) + 1):
    n = int(input())
    graph = [list(input().rstrip().split()) for _ in range(n)]
    answer = list()
    temp = [[0] * n for _ in range(n)]

    for _ in range(3):
        for i in range(n):
            for j in range(n):
                temp[i][j] = graph[(n - 1) - j][i]
        answer.append(deepcopy(temp))
        graph = deepcopy(temp)

    print(f"#{tc}")

    for i in range(n):
        for j in range(3):
            print(''.join(answer[j][i]), end=' ')
        print()