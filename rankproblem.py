import sys
input = sys.stdin.readline
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
print = sys.stdout.write

n, m = map(int, input().strip().split())
positions = [i for i in range(n+1)]
for i in range(m):
    winner, loser = map(lambda x: int(x[1:]), input().strip().split())
    counter = 0
    winner_p, loser_p = -1, -1
    while counter <= n:
        if positions[counter] == loser:
            loser_p = counter
        if positions[counter] == winner:
            winner_p = counter
            break
        counter += 1
    if loser_p == -1:
        continue
    else:
        for j in range(loser_p + 1, winner_p + 1):
            positions[j-1] = positions[j]
        positions[winner_p] = loser
for i in range(1, n+1):
    print(f"T{positions[i]} ")