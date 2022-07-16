# 어디에 단어가 들어갈 수 있을까

# 입력값 : n ( n * n의 배열 ), k : 자릿수

for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    temp = list()
    answer = 0

    for i in range(n):
        temp = [str(item) for item in graph[i]]
        temp = ''.join(temp).split('0')
        
        answer += temp.count('1' * k)

    for j in range(n):
        temp = ''
        for i in range(n):
            temp += str(graph[i][j])
        
        temp = temp.split('0')
        answer += temp.count('1' * k)

    print(f"#{tc} {answer}")
