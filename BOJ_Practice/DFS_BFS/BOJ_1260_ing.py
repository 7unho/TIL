from collections import deque

n, m, v = map(int, input().split())

stack = [0]
graph =[]
graph
for _ in range(n):
    stack.append([])

for _ in range(m):
    a, b = map(int, input().split())
    for i in range(1, n+1):
        if a == i:
            stack[i].append(b)
        if b == i:
            stack[i].append(a)

print(stack)

def dfs(v):
    print(v)



    pass

def bfs(v):
    pass

