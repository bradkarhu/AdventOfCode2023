import sys

def solve(lines: list[str]):
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
    print(winnings)

with open(sys.argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)