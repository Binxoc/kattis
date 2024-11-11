import sys
input = sys.stdin.readline
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
print = sys.stdout.write

def get_rational(n):
    if n == 1:
        return [1, 1]
    prev = get_rational(n//2)
    if n % 2 == 0:
        return [prev[0], prev[0] + prev[1]]
    return [prev[0] + prev[1], prev[1]]

p = int(input().strip())
for i in range(p):
    case, num = input().strip().split()
    print(f"{case} ")
    cur = get_rational(int(num))
    print(f"{cur[0]}/{cur[1]}\n")