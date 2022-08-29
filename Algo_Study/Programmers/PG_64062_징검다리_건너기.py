# 입력값 : stones(징검다리), 한 번에 뛸 수 있는 거리 : K
# 출력값 : 다리를 건널 수 있는 최댓값
import sys
input = sys.stdin.readline
stones = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
k = 3


def solution(stones, k):
    answer = 1
    start = min(stones)
    end = max(stones)
    
    while start <= end:
        mid = (start + end) // 2
        temp = 0
        cnt = 0

        for stone in stones:
            if stone - mid <= 0:
                temp += 1
            elif stone - mid > 0:
                cnt = max(cnt, temp)
                temp = 0
        
        cnt = max(cnt, temp)

        if cnt < k:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1

    return answer

print(solution(stones, k))
