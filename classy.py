import sys
input = sys.stdin.readline
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
print = sys.stdout.write

classes_dict = {
    "upper": -3,
    "middle": -2,
    "lower": -1
}

t = int(input().strip())
for i in range(t):
    people = []
    n = int(input().strip())
    for j in range(n):
        name, classes, _ = input().strip().split()
        class_lst = classes.split("-")
        converted_lst = [classes_dict[x] for x in class_lst[::-1]] + \
            [-2 for x in range(10 - len(class_lst))] + \
            [name[:len(name)-1]]
        people.append(converted_lst)
    people.sort()
    for i in range(n):
        print(f"{people[i][-1]}\n")
    print("==============================\n")