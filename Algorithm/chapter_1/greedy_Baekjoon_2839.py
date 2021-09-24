# 백준 알고리즘 2839_greedy 알고리즘
## 입력 값 N킬로에 대한 설탕 봉투( 5, 3 )의 최소 개수

import sys

input_N = int(sys.stdin.readline())
result = 0

if input_N % 5 == 0:
    result += input_N // 5
else :
    for i in range( 1, (input_N // 3) + 1 ) :
        if ( input_N - (i * 3) ) % 5  == 0:
            result += i + ( (input_N - i * 3) // 5 )
            break

        if i == ( input_N // 3 ) and input_N % 3 == 0:
            result += input_N // 3

print('-1' if result == 0 else result)