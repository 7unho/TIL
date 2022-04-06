import sys
input = sys.stdin.readline

N, C = map(int, input().split())
array = [int(input()) for _ in range(N)]
array.sort()

start = 1
end = max(array) - min(array)

while start <= end:
    mid = (start + end) // 2
    current = array[0]
    count = 1

    for i in range(1, N):
        if array[i] - current >= mid:
            count += 1
            current = array[i]

    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)