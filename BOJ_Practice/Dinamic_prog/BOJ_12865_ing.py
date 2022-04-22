# 평범한 배낭
## K의 무게를 버티는 배낭에 가치가 V인 물건 N개를 입력
## 가치의 최댓값을 출력
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

d = [0 for _ in range(k + 1)]

for i in range(n):
    w, v = map(int, input().split())

    for j in range(w, (k + 1)):
        d[j] = max(d[j], d[j - w] + v)

print(d[k])
