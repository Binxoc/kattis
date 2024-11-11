x = list(map(int, input().strip().split()))
for i in range(6):
    for j in range(i+1, 6):
        for k in range(j+1, 6):
            if x[i] + x[j] + x[k] == x[6]:
                a, b, c = x.pop(k), x.pop(j), x.pop(i)
                lst = sorted([a,b,c], reverse = True) + sorted(x[:3], reverse = True)
                for m in lst:
                    print(f"{m} ", end="")
                exit()