import itertools

arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr, 2)
print(list(nCr))


nPr = itertools.permutations(arr, 2)
nPr = list(nPr)
print(nPr)

arr2 = [1, 2, 3]
subse = []

for i in range(1, len(arr2) + 1):
    subse = subse + list(itertools.combinations(arr, i))

print(subse)