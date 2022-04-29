# # 저울
# ## 입력값 : 측정하려는 값 , 출력값 : 정해진 저울들의 조합으로 할 수 없는 최솟값

# import sys
# input = sys.stdin.readline

# n = int(input())
# weights = list(map(int, input().split()))
# weights.sort()
# answer = 1

# for i in range(1, sum(weights) + 2):
#     if i in weights:
#         continue

#     if i - 

test = [1, 1, 3, 5, 7]
test = list((lambda x : x if x > 4 else 0))
print(test)