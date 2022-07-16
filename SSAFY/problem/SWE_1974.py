# 스도쿠 검증

CHECK = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2

dx = [0, 0, 0, 1, 1, 1, 2, 2, 2]
dy = [0, 1, 2, 0, 1, 2, 0, 1, 2]

for tc in range(1, int(input()) + 1):
    answer = 1
    graph = [list(map(int, input().split())) for _ in range(9)]

    for i in range(9):
        check_X, check_Y = 1, 1
        for j in range(9):
            check_X *= graph[i][j]
            check_Y *= graph[j][i]
        
        if check_X != CHECK or check_Y != CHECK:
                answer = 0
                break
        

    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            check_square = 1
            for k in range(9):
                nx = x + dx[k]
                ny = y + dy[k]
                
                check_square *= graph[nx][ny]
        if check_square != CHECK:
            answer = 0
            break


    print(f"#{tc} {answer}")