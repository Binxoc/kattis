w, s = map(int, input().strip().split())
counter = 1
while counter <= s:
    if (w - 29370 * counter) % 29260 == 0:
        print(counter)
        break
    counter += 1