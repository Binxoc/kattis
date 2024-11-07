import sys
import math
class Scorer:
    def __init__(self, n, results):
        self.n = n
        self.results = results
        self.rubrics = {
            1: 100,
            2: 75,
            3: 60,
            4: 50,
            5: 45,
            6: 40,
            7: 36,
            8: 32,
            9: 29,
            10: 26,
            11: 24,
            12: 22,
            13: 20,
            14: 18,
            15: 16,
            16: 15,
            17: 14,
            18: 13,
            19: 12,
            20: 11,
            21: 10,
            22: 9,
            23: 8,
            24: 7,
            25: 6,
            26: 5,
            27: 4,
            28: 3,
            29: 2,
            30: 1
        }
        self.scores = [-1 for i in range(n)]
    
    def break_tie(self, rank_start, rank_end):
        return math.ceil(sum([self.rubrics.get(i+1, 0) for i in range(rank_start, rank_end)]) / (rank_end - rank_start))
        
    def rank(self):
        self.results.sort(key=lambda x: (-x[0], x[1], x[2]))
        counter = 0
        while counter < self.n:
            check_tie = counter + 1
            while check_tie < self.n:
                if self.results[counter][:3] == self.results[check_tie][:3]:
                    check_tie += 1
                else:
                    break
            tied_score = self.break_tie(counter, check_tie)
            for i in range(counter, check_tie):
                self.scores[i] = [tied_score + self.results[i][3], self.results[i][4]]
            counter = check_tie
    
    def output_scores(self):
        self.scores.sort(key=lambda x: x[1])
        for i in range(self.n):
            print(self.scores[i][0])

if __name__ == "__main__":
    input = sys.stdin.readline
    results = []
    n = int(input())
    for i in range(n):
        cur = list(map(int, input().split()))
        cur.append(i)
        results.append(cur)
        
    # n = 5
    # results = [
    #     [6, 390, 112, 1, 0],
    #     [5, 280, 97, 0, 1],
    #     [4, 79, 45, 1, 2],
    #     [4, 94, 49, 1, 3],
    #     [4, 126, 55, 1, 4]
    # ] 
    
    scorer = Scorer(n, results)
    scorer.rank()
    scorer.output_scores()