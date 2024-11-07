import sys

class Frogger():
    def __init__(self, n, squares):
        self.n = n
        self.squares = list(map(lambda x: [x, False], squares))
    
    def play_game(self, start, magic):
        hops = 0
        self.squares[start][1] = True
        while True:
            if self.squares[start][0] == magic:
                return "magic", hops
            else:
                hops += 1
                if start + self.squares[start][0] < 0:
                    return "left", hops
                elif start + self.squares[start][0] >= self.n:
                    return "right", hops
                else:
                    start += self.squares[start][0]
                    if self.squares[start][1]:
                        return "cycle", hops
                    self.squares[start][1] = True

if __name__ == "__main__":
    input = sys.stdin.readline
    n, start, magic = list(map(int, input().split()))
    frogger = Frogger(n, list(map(int, input().split())))
    fate, hops = frogger.play_game(start - 1, magic)
    print(f"{fate}\n{hops}")