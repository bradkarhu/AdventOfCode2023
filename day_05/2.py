from sys import argv

def solve(lines: list[str]):
    seeds = lines[0].split(":")[1].strip().split()
    ranges = []
    for x in range(0, len(seeds)//2):
        start = int(seeds[2*x])
        stop = start + int(seeds[2*x+1])
        ranges.append(range(start, stop))
    maps = get_maps(lines)
    for map in maps:
        ranges = get_ranges(map, ranges)
    min = 1e32
    for rg in ranges:
        if rg.start < min: min = rg.start
    print(min)

def get_maps(lines: list[str]) -> list[list[tuple]]:
    maps = []
    index = 2
    while index + 1 < len(lines):
        map, index = get_map(lines, index + 1)
        maps.append(map)
    return maps

def get_map(lines: list[str], index: int) -> [list[tuple], int]:
    tuples = []
    while index < len(lines) and lines[index] != "":
        # destination_range_start source_range_start range_length
        d, s, r = lines[index].split()
        tuples.append((int(d), int(s), int(r)))
        index += 1 # next line
    index += 1 # skip blank line
    tuples = sorted(tuples, key=lambda x: x[1]) # sort by source_range_start
    return tuples, index

def get_ranges(map: list[tuple], source_ranges: list[range]) -> int:
    destination_ranges = []
    for d, s, r in map:
        outside_ranges = []
        while source_ranges:
            rg = source_ranges.pop()
            before = range(rg.start, min(rg.stop, s))
            x1 = max(rg.start, s)
            x2 = min(rg.stop, s + r)
            after = range(max(rg.start, s + r), rg.stop)
            if before.start < before.stop:
                outside_ranges.append(before)
            if x1 < x2:
                y1 = d + x1 - s
                y2 = d + x2 - s
                destination_ranges.append(range(y1, y2))
            if after.start < after.stop:
                outside_ranges.append(after)
        source_ranges = outside_ranges
    return source_ranges + destination_ranges

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)