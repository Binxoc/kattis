import sys

def get_closest_99(val):
    if val < 100:
        return 99
    if val % 100 >= 49:
        return (val // 100) * 100 + 99
    return (val // 100 - 1) * 100 + 99

input = sys.stdin.readline
print = sys.stdout.write
print(str(get_closest_99(int(input().strip()))))