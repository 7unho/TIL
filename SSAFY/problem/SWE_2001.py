# 파리 퇴치

# 입력값 : N * N의 배열, M * M의 파리채, 출력값 : 파리채 범위의 최댓값

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(n)]
    answer = 0

    for i in range((n - m) + 1):
        for j in range((n - m) + 1):
            temp = 0

            for k in range(m):
                temp += sum(graph[i + k][j:j + m])
            
            answer = max(answer, temp)
    
    print(f"#{tc} {answer}")