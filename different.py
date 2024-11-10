while True:
    try:
        cur = input()
    except EOFError:
        break
    n1, n2 = map(int, cur.strip().split())
    print(abs(n1-n2))