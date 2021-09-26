# K층에 N호
t = int(input())
result = []


for t_Count in range(t):
    k = int(input())
    n = int(input())
    pre_floor = [1 for _ in range(n)]
    cur_floor = []
    print(pre_floor)

    if n == 1:
        result = 1
    else:
        for k_Count in range(k):
            for i in range(n):
                cur_floor.append(sum(pre_floor[:i + 1]))
            result.append(cur_floor[n - 1])

print(result)



