n = int(input())
primes = []
for i in range(2, int(n**0.5) + 2):
    if n % i == 0:
        primes.append(i)

if not primes:
    print(1)
else:
    points = 0
    for prime in primes:
        while n % prime == 0:
            n /= prime
            points += 1
    if n > 1:
        points += 1
    print(points)