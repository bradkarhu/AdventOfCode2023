import sys

def solve(lines: list[str]):
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
    for i in range(0, num_cards):
        for j in range(0, match_array[i]):
            cards_array[i+j+1] += cards_array[i]
    #print(f'cards: {cards_array}')
    print(sum(cards_array))

with open(sys.argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)