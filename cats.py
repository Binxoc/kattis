import sys
input = sys.stdin.readline
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
print = sys.stdout.write

class UFDS:
    def __init__(self, n):
        self.ufds = [i for i in range(n+1)]
        self.rank = [0 for i in range(n+1)]
    
    def findset(self, x):
        if self.ufds[x] == x:
            return x
        self.ufds[x] = self.findset(self.ufds[x])
        return self.ufds[x]

    def isSameSet(self, x, y):
        return self.findset(x) == self.findset(y)
    
    def unionSet(self, x, y):
        p, q = self.findset(x), self.findset(y)
        if p != q:
            if self.rank[p] > self.rank[q]:
                self.ufds[q] = p
            else:
                self.ufds[p] = q
                if self.rank[p] == self.rank[q]:
                    self.rank[q] += 1

t = int(input().strip())
for i in range(t):
    m, c = map(int, input().strip().split())

    edge_list = []
    ufds = UFDS(c)
    for j in range(c*(c-1)//2):
        edge_list.append(list(map(int, input().strip().split())))
    edge_list.sort(key=lambda x: x[2])

    mst_sum = 0
    v = 0
    counter = 0
    while v < c-1:
        x, y, w = edge_list[counter]
        if not ufds.isSameSet(x, y):
            mst_sum += w
            v += 1
            ufds.unionSet(x, y)
        counter += 1
    
    if mst_sum + c <= m:
        print("yes\n")
    else:
        print("no\n")