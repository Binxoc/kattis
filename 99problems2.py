import sys
import io
import os
import datetime as dt
import bisect

start = dt.datetime.now()

def binary_search(val, cond, diff, tracker):
    if cond == 1:
        insert_index = bisect.bisect_left(diff, val)
        if insert_index == n and val > diff[-1]:
            return -1
        elif insert_index == n:
            insert_index -= 1
    else:
        insert_index = bisect.bisect_right(diff, val)
        if insert_index > 0:
            insert_index -= 1

    tracker_index = tracker[insert_index][0]
    if cond == 1:
        while tracker_index < n and tracker[tracker_index][1] == 0:
            tracker_index += 1
        if tracker_index < n and tracker[tracker_index][1] == 1:
            tracker[tracker_index][1] -= 1
            tracker[insert_index][0] = tracker_index
            return diff[tracker_index]
        else:
            return -1
    else: 
        while tracker_index >= 0 and tracker[tracker_index][1] == 0:
            tracker_index -= 1
        if tracker_index >= 0 and tracker[tracker_index][1] == 1:
            tracker[tracker_index][1] -= 1
            tracker[insert_index][0] =  tracker_index
            return diff[tracker_index]
        else:
            return -1

if __name__ == "__main__":
    input = sys.stdin.readline
    # input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    print = sys.stdout.write
    n, q = list(map(int, input().strip().split()))
    diff = list(map(int, input().strip().split()))
    diff.sort()
    tracker = [[i, 1] for i in range(n)]
    for i in range(q):
        cond, val = list(map(int, input().strip().split()))
        if cond == 1:
            val += 1
        print(str(binary_search(val, cond, diff, tracker)) + "\n")
    
    print(str(dt.datetime.now() - start))