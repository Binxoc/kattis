import sys
input = sys.stdin.readline
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
print = sys.stdout.write

n, x = map(int, input().strip().split())
prices = list(map(int, input().strip().split()))
prices.sort(reverse=True)
counter = 0
while counter < n - 1:
    if prices[counter] + prices[counter + 1] > x:
        counter += 1
    else:
        break
print(str(n - counter))
