import sys
class Sequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def count_inversions(self):
        total_inversions, one_counter, num_sub_sequences = 0, 0, 1
        for i in range(len(self.sequence)):
            if self.sequence[i] == "0":
                total_inversions = (total_inversions + one_counter) % 1000000007
            elif self.sequence[i] == "1":
                one_counter = (one_counter + num_sub_sequences) % 1000000007
            else:
                total_inversions = (2 * total_inversions + one_counter) % 1000000007
                one_counter = (2 * one_counter + num_sub_sequences) % 1000000007
                num_sub_sequences = (2 * num_sub_sequences) % 1000000007
        return total_inversions

    
if __name__ == "__main__":
    input = sys.stdin.readline
    sequence = Sequence(input().strip())
    print(sequence.count_inversions())