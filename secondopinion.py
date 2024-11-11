n = int(input())
h, m, s = n // 3600, (n % 3600) // 60, (n % 3600) % 60
print(f"{h} : {m} : {s}")
