# 최적의 행렬 곱셈
def solution(sizes):
    dp = [[0 for _ in range(len(sizes))] for _ in range(len(sizes))]

    # gap = 
    for gap in range(1, len(sizes)):
        for s in range(len(sizes) - gap):
            e = s + gap

            temp = list()

            for m in range(s, e):
                temp.append(dp[s][m] + dp[m + 1][e] + sizes[s][0] * sizes[m][1] * sizes[e][1])
            
            dp[s][e] = min(temp)
    
    return dp[0][-1]

matrix_sizes = [[5, 3], [3, 10], [10, 6]]
print(solution(matrix_sizes))
