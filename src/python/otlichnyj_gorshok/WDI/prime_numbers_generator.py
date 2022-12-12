primenumbers = {}


def eratostenes(n):
    arr = [True] * (n + 1)
    arr[0] = arr[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        for x in range(2 * i, n + 1, i):
            arr[x] = False
    return arr

n = int(input("do ktorej liczby\n"))
num = eratostenes(n)
primes = [i for i in range(n+1) if(num[i])]
print(primes)