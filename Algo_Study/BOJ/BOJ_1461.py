# 도서관
## 입력값 : 책의 개수 (N), 세준이가 한 번에 들 수 있는 책의 개수 (M)

import sys
input = sys.stdin.readline

def make_answer(list):
    global M
    if len(list) >= M:
        sum += sum(list[:M])
        return (sum, list[M:].copy())
    sum += sum(list)
    return (sum, [])

global M
N, M = map(int, input().split())
positive, negative = list(), list()

input = list(map(int, input().split()))

# 음수, 양수 리스트 분리
for item in input:
    if item > 0 :
        positive.append(item)
        continue
    negative.append(item)

# 각 리스트 정렬
positive.sort(reverse=True)
negative.sort()

# 최댓값 도출 후, answer 초기화
param = positive if positive[0] > -negative[0] else negative
answer  = make_answer(param)[0]


