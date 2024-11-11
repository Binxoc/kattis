import sys
input = sys.stdin.readline
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
print = sys.stdout.write

n, t = map(int, input().strip().split())
times = []
for i in range(n):
    times.append(int(input().strip()))
times.sort()
possible = True
for i in range(n):
    if times[i] - (t * i) <= 0:
        possible = False

if possible:
    print("YES")
else:
    print("NO")