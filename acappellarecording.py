import sys
input = sys.stdin.readline
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
print = sys.stdout.write

n, diff = map(int, input().strip().split())
pitches = []
for i in range(n):
    pitches.append(int(input().strip()))
pitches.sort()

min_recordings = 0
counter = 0
while counter < n:
    min_recordings += 1
    cur_min, cur_max = pitches[counter], pitches[counter] + diff
    while counter < n and pitches[counter] <= cur_max:
        counter += 1
print(str(min_recordings))