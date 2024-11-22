x = sorted(list(map(int, input().strip().split())))
order = input().strip()
for y in order:
    if y == "A":
        print(f"{x[0]} ", end="")
    elif y == "B":
        print(f"{x[1]} ", end="")
    elif y == "C":
        print(f"{x[2]} ", end="")