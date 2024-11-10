n = int(input().strip())

days = 0
while 2 ** days < n:
    days += 1
print(days + 1)