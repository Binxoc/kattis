import sys

dp = [False for i in range(513)]
permutations = []
operations = {0: "*", 1: "+", 2: "-", 3: "/"}
for i in range(4):
    for j in range(4):
        for k in range(4):
            permutations.append([operations[i], operations[j], operations[k]])
for p in permutations:
    stack1, stack2 = [4],  []
    counter = 0
    while counter <= 2:
        if p[counter] == "*":
            stack1.append(stack1.pop() * 4)
        elif p[counter] == "/":
            stack1.append(stack1.pop() // 4)
        else:
            stack1.append(p[counter])
            stack1.append(4)
        counter += 1
    while stack1:
        stack2.append(stack1.pop())
    res = stack2.pop()
    while stack2:
        operator, cur = stack2.pop(), stack2.pop()
        if operator == "+":
            res += cur
        else:
            res -= cur
    dp[res + 256] = p

input = sys.stdin.readline
n = int(input().strip())
for i in range(n):
    cur = int(input().strip())
    if cur > 256 or cur < -256:
        print("no solution")
    else:
        operators = dp[cur + 256]
        if not operators:
            print("no solution")
            continue
        print(str(4) + " ", end="")
        for i in range(3):
            print(operators[i] + " ", end="")
            print(str(4) + " ", end="")
        print("= " + str(cur))