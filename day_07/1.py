import sys

def solve(lines: list[str]):
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
    print(winnings)

with open(sys.argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)