import time

class Part1:
    @staticmethod
    def solution(lines: list[str]) -> int:
        sum = 0
        for line in iter(lines):
            data = line.split(":")[1].strip()
            index = data.find("|")
            winners = data[:index].strip().split()
            numbers = data[index+1:].strip().split()
            #print(f'winners = {winners}')
            #print(f'numbers = {numbers}')
            matches = set(winners) & set(numbers)
            if len(matches) > 0:
                points = pow(2, len(matches) - 1)
                #print(f'{matches} = {points} points')
                sum += points
        return sum

class Part2:
    @staticmethod
    def solution(lines: list[str]) -> int:
        num_cards = len(lines)
        match_array = [0] * num_cards
        cards_array = [1] * num_cards
        for i in range(0, num_cards):
            line = lines[i]
            data = line.split(":")[1].strip()
            index = data.find("|")
            winners = data[:index].strip().split()
            numbers = data[index+1:].strip().split()
            matches = set(winners) & set(numbers)
            match_array[i] = len(matches)
        #print(f'matches: {match_array}')
        # [4, 2, 2, 1, 0, 0] MATCHES
        # [1, 1, 1, 1, 1, 1] CARDS
        #  4:+1 +1 +1 +1
        # [1, 2, 2, 2, 2, 1] CARDS
        #     2:+2 +2
        # [1, 2, 4, 4, 2, 1] CARDS
        #        2:+4 +4
        # [1, 2, 4, 8, 6, 1] CARDS
        #           1:+8
        # [1, 2, 4, 8,14, 1] CARDS
        for i in range(0, num_cards):
            for j in range(0, match_array[i]):
                cards_array[i+j+1] += cards_array[i]
        #print(f'cards: {cards_array}')
        return sum(cards_array)

tic = time.perf_counter()
with open("input.txt", "r") as file:
    f = file.read().splitlines()
print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
#Part 1: 25183
#Part 2: 5667240
#Took 0.0013 seconds