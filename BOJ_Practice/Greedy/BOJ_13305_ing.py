# 주유소

from math import dist
import sys
input = sys.stdin.readline

n = int(input())

dist_list = list(map(int, input().split()))
city_list = list(map(int, input().split()))
city_list.insert(0, 0)

d = [0 for _ in range(n + 1)]
d[2] = dist_list[0] + city_list[0]

for i in range(3, n + 1):
    d[i] = d[i - 1] + max(city_list[i - 2], city_list[i - 1]) * dist_list[i - 1]

print(d)