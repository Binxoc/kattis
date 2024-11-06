import sys
import math
import copy

class Multiplier:
    def __init__(self):
        self.num1, self.num2, self.dim, self.products, self.diagonals = -1, -1, [], [], []
    
    def set_params(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.dim = [len(str(num2)), len(str(num1))]
        self.products = [[[0,0] for i in range(self.dim[1])] for i in range(self.dim[0])]
    
    def reset_params(self):
        self.num1, self.num2, self.dim, self.products, self.diagonals = -1, -1, [], [], []
    
    def calculate_diagonals(self):
        products_copy = copy.deepcopy(self.products)
        to_divide = 0
        if self.dim[0] > self.dim[1]:
            for i in range(self.dim[0]):
                for j in range(self.dim[0] - self.dim[1]):
                    products_copy[i].append([0,0])
            to_divide = self.dim[0] - self.dim[1]        
        elif self.dim[1] > self.dim[0]:
            for i in range(self.dim[1] - self.dim[0]):
                products_copy.append([[0,0] for i in range(self.dim[1])])
            to_divide = self.dim[1] - self.dim[0]
        
        for i in range(len(products_copy) * 2):
            num = 2 * i if i + 1 <= len(products_copy) else (2 * len(products_copy) - i - 1) * 2
            diagonal_sum = products_copy[i//2][i//2][i%2]
            tracker1, tracker2 = [i//2, i//2, i%2], [i//2, i//2, i%2]
            while num > 0:
                if tracker1[2]:
                    tracker1[0] += 1
                    tracker1[2] = 0
                    tracker2[1] += 1
                    tracker2[2] = 0
                else:
                    tracker1[1] -= 1
                    tracker1[2] = 1
                    tracker2[0] -= 1
                    tracker2[2] = 1
                diagonal_sum += products_copy[tracker1[0]][tracker1[1]][tracker1[2]]
                diagonal_sum += products_copy[tracker2[0]][tracker2[1]][tracker2[2]]
                num -= 2
            self.diagonals.append(diagonal_sum)
        for i in range(len(self.diagonals) - 1, 0, -1):
            if self.diagonals[i] > 9:
                self.diagonals[i-1] += self.diagonals[i] // 10
                self.diagonals[i] = self.diagonals[i] % 10
        self.diagonals = self.diagonals[: len(self.diagonals) - to_divide]
    
    def output_lattice(self):
        top_and_bottom = "+---" + self.dim[1] * "----" + "+"
        print(top_and_bottom)
        
        print("|   ", end="")
        for i in range(self.dim[1]):
            print(str(self.num1)[i] + "   ", end="")
        print("|")
        
        def inner_matrix():
            print("| +" + self.dim[1] * "---+" + " |")
            first = False
            for i in range(self.dim[0]):
                counter = 1
                while counter < 4:
                    if counter == 2:
                        print("| " + self.dim[1] * "| / " + "|" + str(self.num2)[i] + "|")
                    elif counter == 1:
                        if first:
                            print("|/|", end="")
                        else:
                            print("| |", end="")
                            if self.diagonals[i]:
                                first = True
                        for j in range(self.dim[1]):
                            print(str(self.products[i][j][0]) + " /|", end="")
                        print(" |")
                    elif counter == 3:
                        print("|" + str(self.diagonals[i]) + "|", end="") if self.diagonals[i] else print("| |", end="")
                        for j in range(self.dim[1]):
                            print("/ " + str(self.products[i][j][1]) + "|", end="")
                        print(" |")
                        print("| +" + self.dim[1] * "---+" + " |")
                    counter += 1
        
        inner_matrix()
        
        print("|", end="")
        for i in range(self.dim[0], self.dim[0] + self.dim[1]):
            if i == 1 and not self.diagonals[0]:
                print("  " + str(self.diagonals[i]) + " ", end="")
            else:
                print("/ " + str(self.diagonals[i]) + " ", end="")
        print("   |")
        print(top_and_bottom)
    
    def get_lattice(self, num1, num2):
        self.set_params(num1, num2)
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                num1_operand = int(str(self.num1)[j])
                num2_operand = int(str(self.num2)[i])
                self.products[i][j][0], self.products[i][j][1] = (num1_operand * num2_operand) // 10, (num1_operand * num2_operand) % 10
        self.calculate_diagonals()
        self.output_lattice()
        self.reset_params()

if __name__ == "__main__":
    input = sys.stdin.readline
    num1, num2 = list(map(int, input().split()))
    multiplier = Multiplier()
    while num1 != 0 and num2 != 0:
        multiplier.get_lattice(num1, num2)
        num1, num2 = map(int, input().split())