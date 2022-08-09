# 도서관
## 입력값 : 책의 개수 (N), 세준이가 한 번에 들 수 있는 책의 개수 (M)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

array = list(map(int, input().split()))

# 음수, 양수 리스트 분리
negative = list()
positive = list()
answers = list()

# 초기화
for item in array:
    if item < 0:
        negative.append(item)
        continue
    positive.append(item)

# 절댓값이 최댓값인 순으로 내림차순 정렬
negative.sort()
positive.sort(reverse=True)

print(negative)
print(positive)

# 가장 멀리 있는 값 서치
## 왕복하지 않기 위해
maximum = 0

for item in array:
    maximum = max(abs(maximum), abs(item))

## positive, negative를 순회하면서, maximum이 아니라면 answers에 append
for i in range(0, len(positive), M):
    if abs(positive[i]) != maximum:
        answers.append(positive[i])

for i in range(0, len(negative), M):
    if abs(negative[i]) != maximum:
        answers.append(negative[i])

answer = maximum

# 왕복하므로 item * 2 연산
for item in answers:
    answer += abs(item * 2)

print(answer)