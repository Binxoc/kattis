import sys 
class Zone:
    def __init__(self, r, c, graph):
        self.r = r
        self.c = c
        self.graph = graph
        self.visited = [[False for i in range(self.c)] for i in range(self.r)]
        self.cluster = [[-1 for i in range(self.c)] for i in range(self.r)]
        
    # def dfs(self, r1, c1, cluster):
    #     if self.visited[r1][c1]:
    #         return
    #     self.visited[r1][c1] = True
    #     self.cluster[r1][c1] = cluster
    #     b_or_d = self.graph[r1][c1]
    #     if r1 > 0 and self.graph[r1 - 1][c1] == b_or_d and not self.visited[r1 - 1][c1]:
    #         self.dfs(r1 - 1, c1, cluster)
    #     if r1 < self.r - 1 and self.graph[r1 + 1][c1] == b_or_d and not self.visited[r1 + 1][c1]:
    #         self.dfs(r1 + 1, c1, cluster)
    #     if c1 > 0 and self.graph[r1][c1 - 1] == b_or_d and not self.visited[r1][c1 - 1]:
    #         self.dfs(r1, c1 - 1, cluster)   
    #     if c1 < self.c - 1 and self.graph[r1][c1 + 1] == b_or_d and not self.visited[r1][c1 + 1]:
    #         self.dfs(r1, c1 + 1, cluster)
    
    def bfs(self, r1, c1, cluster):
        self.visited[r1][c1] = True
        self.cluster[r1][c1] = cluster
        b_or_d = self.graph[r1][c1]
        neighbours = [(r1-1, c1), (r1+1, c1), (r1, c1-1), (r1, c1+1)]
        counter = 0
        while counter < len(neighbours):
            cur_r, cur_c = neighbours[counter][0], neighbours[counter][1]
            counter += 1
            if cur_r < 0 or cur_r >= self.r or cur_c < 0 or cur_c >= self.c:
                continue
            if not self.visited[cur_r][cur_c] and self.graph[cur_r][cur_c] == b_or_d:
                self.visited[cur_r][cur_c] = True
                self.cluster[cur_r][cur_c] = cluster
                neighbours.append((cur_r-1, cur_c))
                neighbours.append((cur_r+1, cur_c))
                neighbours.append((cur_r, cur_c-1))
                neighbours.append((cur_r, cur_c+1))

    def process_cluster(self):
        cluster = 1
        for i in range(self.r):
            for j in range(self.c):
                if not self.visited[i][j]:
                    self.bfs(i, j, cluster)
                    cluster += 1

    def check_visited(self, r1, c1, r2, c2):
        if self.cluster[r1][c1] != self.cluster[r2][c2]:
            return "neither"
        else:
            if self.graph[r2][c2]:
                return "decimal"
            else:
                return "binary"

if __name__ == "__main__":
    input = sys.stdin.readline
    r, c = map(int, input().strip().split())
    graph = []
    # graph = [[1 for i in range(1000)] for i in range(1000)]
    for i in range(r):
        graph.append(list(map(int, list(input().strip()))))
    zone = Zone(r, c, graph)
    zone.process_cluster()
    for i in range(int(input().strip())):
        r1, c1, r2, c2 = list(map(int, input().strip().split()))
        print(zone.check_visited(r1 - 1, c1 - 1, r2 - 1, c2 - 1))