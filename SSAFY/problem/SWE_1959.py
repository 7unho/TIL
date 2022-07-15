# 두 개의 숫자열

for tc in range(int(input())):
    n, m = map(int, input().split())
    answer = 0

    arr = list()
    arr.append(list(map(int, input().split())))
    arr.append(list(map(int, input().split())))

    arr.sort(key=lambda x: len(x))

    for i in range(abs(n - m) + 1):
        sum = 0
        for j in range(min(n, m)):
            sum += arr[0][j] * arr[1][i + j]
        
        answer = max(answer, sum)

    print(f"#{tc + 1} {answer}")
