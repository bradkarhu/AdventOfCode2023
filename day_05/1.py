from sys import argv

def solve(lines: list[str]):
    min = -1
    seeds = lines[0].split(":")[1].strip().split()
    maps = get_maps(lines)
    for seed in iter(seeds):
        # see if any sets contains the seed
        source = int(seed)
        for map in iter(maps):
            source = get_destination(map, source)
        location = source
        #print(f'Seed {seed} => Location {location}')
        if min == -1 or location < min: min = location
    print(min)

def get_maps(lines: list[str]) -> list[list[tuple]]:
    maps = []
    index = 2
    while index + 1 < len(lines):
        map, index = get_map(lines, index + 1)
        maps.append(map)
    return maps

def get_map(lines: list[str], index: int) -> [list[tuple], int]:
    d = []; s = []; r = []
    while index < len(lines) and lines[index] != "":
        # destination_range_start source_range_start range_length
        split = lines[index].split()
        d.append(int(split[0]))
        s.append(int(split[1]))
        r.append(int(split[2]))
        index += 1 # next line
    index += 1 # skip blank line
    return list(zip(d, s, r)), index

def get_destination(map: list[tuple], source: int) -> int:
    destination = -1
    for t in iter(map):
        # test that our source fails within the range
        if source >= t[1] and source < t[1]+t[2]:
            # get the destination value
            x = t[0] + (source - t[1])
            if destination == -1 or x < destination:
                destination = x
    if destination == -1: destination = source
    #print(f'{source} -> {destination}')
    return destination

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)