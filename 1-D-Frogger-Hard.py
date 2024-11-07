import sys

class Frogger():
    def __init__(self, n, squares):
        self.n = n
        self.squares = squares
        self.visited = [False for i in range(n)]
        self.track_magic_nums = dict([i, {}] for i in range(n))

    def toposort(self):
        order = [[i, 0] for i in range(self.n)]
        for i in range(self.n):
            next = i + self.squares[i]
            if not(next < 0 or next >= self.n):
                order[next][1] += 1
        order.sort(key = lambda x: x[1])
        return list(map(lambda x: x[0], order))

    def count_winning_instances(self):
        count = 0
        order = self.toposort()
        for i in order:
            if self.visited[i]:
                continue
            cur_search = [i]
            cur_visited = {}
            self.visited[i] = True
            count += 1
            self.track_magic_nums[i][self.squares[i]] = True
            counter = i
            cycle = False
            while True:
                counter += self.squares[counter]
                if counter < 0 or cycle or counter >= self.n or cur_visited.get(counter, False):
                    break
                cur_visited[counter] = True
                if not self.visited[counter]:
                    cur_search.append(counter)
                    self.visited[counter] = True
                for j in cur_search:
                    if not self.track_magic_nums[j].get(self.squares[counter], False):
                        count += 1
                        self.track_magic_nums[j][self.squares[counter]] = True
                if counter == i:
                    cycle = True
        return count

if __name__ == "__main__":
    input = sys.stdin.readline
    n = list(map(int, input().split()))[0]
    frogger = Frogger(n, list(map(int, input().split())))
    print(frogger.count_winning_instances())