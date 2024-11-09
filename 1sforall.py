import sys
import math
class Complexity:
    def __init__(self, num):
        self.num = num
        self.dp = [float("inf") for i in range(num+1)]
        self.dp[0], self.dp[1] = 0, 1
        
    def get_complexity(self):
        for i in range(2, self.num+1):
            for k in range(1, i//2+1):
                self.dp[i] = min(self.dp[i], self.dp[i-k] + self.dp[k])
            for k in range(1, int(math.sqrt(i)) + 1):
                if not i % k:
                    self.dp[i] = min(self.dp[i], self.dp[i // k] + self.dp[k])
            for k in range(1, int(len(str(i)))):
                if str(i)[k] != "0":
                    self.dp[i] = min(self.dp[i], self.dp[int(str(i)[:k])] + self.dp[int(str(i)[k:])])
        return self.dp[self.num]
            
if __name__ == "__main__":
    input = sys.stdin.readline
    # print(Complexity(20).get_complexity())
    print(Complexity(int(input().strip())).get_complexity())