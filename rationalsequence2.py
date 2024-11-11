import sys
input = sys.stdin.readline
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
print = sys.stdout.write

p = int(input().strip())
for i in range(p):
    case, num = input().strip().split()
    num1, num2 = list(map(int, num.split("/")))
    traverse = []
    while num1 != num2:
        if num1 > num2:
            traverse.append(2)
            num1 -= num2
        else:
            traverse.append(1)
            num2 -= num1
    
    traverse.reverse()
    cur = 1
    for i in traverse:
        if i == 1:
            cur *= 2
        else:
            cur = 2 * cur + 1

    print(f"{case} {cur}\n")