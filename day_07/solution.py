import time

class Part1:
    @staticmethod
    def solution(lines: list[str]) -> int:
        sets = [[],[],[],[],[],[],[]] # high card -> five of a kind
        for line in iter(lines):            
            cards = [0] * 13
            cards_s = ""
            for i in range(0, 5):
                char = line[i]
                d = 0                
                if char == 'A': d = 12
                elif char == 'K': d = 11
                elif char == 'Q': d = 10
                elif char == 'J': d = 9
                elif char == 'T': d = 8
                else: d = int(char) - 2
                cards[d] += 1
                cards_s += chr(d + 97) # start at 'a'
            line = cards_s + line[5:]
            pairs = []
            for c in range(13):
                if cards[c] > 1: 
                    pairs.append(cards[c])
            num = len(pairs)
            if num == 2:
                if pairs[0] == 3 or pairs[1] == 3: sets[4].append(line) # full house
                else: sets[2].append(line) # two pair
            elif num == 1:
                if pairs[0] == 5: sets[6].append(line) # five of a kind
                elif pairs[0] == 4: sets[5].append(line) # four of a kind
                elif pairs[0] == 3: sets[3].append(line) # three of a kind
                else: sets[1].append(line) # one pair
            else:
                sets[0].append(line) # high card
        for i in range(len(sets)):
            sets[i] = sorted(sets[i])
        rank = 1
        winnings = 0
        for set in iter(sets):
            for line in iter(set):
                bid = int(line[6:])
                winnings += rank * bid
                rank += 1
        return winnings

class Part2:
    @staticmethod
    def solution(lines: list[str]) -> int:
        sets = [[],[],[],[],[],[],[]] # high card -> five of a kind
        for line in iter(lines):
            wilds = 0
            cards = [0] * 13            
            cards_s = ""
            for i in range(0, 5):
                char = line[i]
                d = 0                
                if char == 'A': d = 12
                elif char == 'K': d = 11
                elif char == 'Q': d = 10
                elif char == 'J': d = 0; wilds += 1 # jokers are wild, also the weakest
                elif char == 'T': d = 9
                else: d = int(char) - 1
                cards[d] += 1
                cards_s += chr(d + 97) # start at 'a'
            line = cards_s + line[5:]
            pairs = []
            for c in range(1,13): # skip wilds
                if cards[c] > 1: 
                    pairs.append(cards[c])
            pairs = sorted(pairs, reverse=True)
            num = len(pairs)
            a = pairs[0] if num > 0 else 0
            b = pairs[1] if num > 1 else 0
            if wilds > 0:
                if a == 0: a = min(a + wilds + 1, 5)
                else: a = min(a + wilds, 5)
            if a == 5: sets[6].append(line) # five of a kind
            elif a == 4: sets[5].append(line) # four of a kind
            elif a == 3 and b == 2: sets[4].append(line) # full house
            elif a == 3: sets[3].append(line) # three of a kind
            elif a == 2 and b == 2: sets[2].append(line) # two pair
            elif a == 2: sets[1].append(line) # one pair
            else: sets[0].append(line) # high card
        for i in range(len(sets)):
            sets[i] = sorted(sets[i])
        rank = 1
        winnings = 0
        #types = ["high card", "one pair", "two pair", "three of a kind", "full house", "four of a kind", "five of a kind"]
        for i in range(len(sets)):
            set = sets[i]
            #print(f'######### {types[i]} ##########')
            for line in iter(set):
                bid = int(line[6:])
                #print(f'{line[:5]} = {bid} * {rank}')
                winnings += rank * bid
                rank += 1
        return winnings

#class Helper:

tic = time.perf_counter()
#with open("better_sample.txt", "r") as file:
#with open("sample.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()
print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
#Part 1: 252656917
#Part 2: 253499763
#Took 0.0043 seconds