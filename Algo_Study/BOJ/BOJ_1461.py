# 도서관
## 입력값 : 책의 개수 (N), 세준이가 한 번에 들 수 있는 책의 개수 (M)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

array = list(map(int, input().split()))

# 음수, 양수 리스트 분리
negative = list()
positive = list()

# 초기화
for item in array:
    if item < 0:
        negative.append(item)
        continue
    positive.append(item)

# 절댓값이 최댓값인 순으로 내림차순 정렬
negative.sort()
positive.sort(reverse=True)

n_temp = list()
p_temp = list()

for i in range(0, len(negative), M):
    n_temp.append(abs(negative[i]))

for i in range(0, len(positive), M):
    n_temp.append(abs(positive[i]))

answer = 0
maximum = 0

if n_temp:
    maximum = max(n_temp[0], maximum)

if p_temp:
    maximum = max(p_temp[0], maximum)
    
answer = ((sum(n_temp) + sum(p_temp) * 2) - maximum)

print(answer)