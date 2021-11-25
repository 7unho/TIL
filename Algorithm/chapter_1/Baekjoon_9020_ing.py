t = int(input())

def isPrime(num):
    if 0 < num <= 2:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


for i in range(t):
    n = int(input())
    pass


