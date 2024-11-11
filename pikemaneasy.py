n, x = map(int, input().strip().split())
a, b, c, t = map(int, input().strip().split())

times = [t]

def get_time(t):
    return (a * t + b) % c + 1

for i in range(n-1):
    t = get_time(t)
    times.append(t)

times.sort()

total_penalty = 0
penalty = times[0]
solved = 0
while penalty <= x:
    solved += 1
    total_penalty = (total_penalty + penalty) % 1000000007
    if solved == n:
        break
    penalty = penalty + times[solved]

print(f"{solved} {total_penalty}")