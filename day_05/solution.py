import time

class Part1:
    @staticmethod
    def solution(lines: list[str]) -> int:
        min = -1
        seeds = lines[0].split(":")[1].strip().split()
        maps = Helper.get_maps(lines)
        for seed in iter(seeds):
            # see if any sets contains the seed            
            source = int(seed)
            for map in iter(maps):
                source = Helper.get_destination(map, source)
            location = source
            #print(f'Seed {seed} => Location {location}')
            if min == -1 or location < min: min = location
        return min

class Part2:    
    @staticmethod
    def solution(lines: list[str]) -> int:
        min = -1
        pairs = lines[0].split(":")[1].strip().split()
        num_pairs = int(len(pairs)/2)
        maps = Helper.get_maps(lines)
        for x in range(0, num_pairs):
            start = int(pairs[2*x])
            stop = start + int(pairs[2*x+1])
            #s, r = Helper.get_source_ranges(lines, 2)
            for seed in range(start, stop):
                # see if any sets contains the seed
                source = int(seed)
                for map in iter(maps):
                    source = Helper.get_destination(map, source)
                location = source
                #print(f'Seed {seed} => Location {location}')
                if min == -1 or location < min: min = location
            print(f'pair {x+1} of {num_pairs}: minimum = {min}')
        return min

class Helper:
    def get_maps(lines: list[str]) -> list[list[tuple]]:
        maps = []
        index = 2
        while index + 1 < len(lines):
            map, index = Helper.get_map(lines, index + 1)
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

tic = time.perf_counter()
#with open("sample.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()
print(f"Part 1: {Part1.solution(f)}")
#print(f"Part 2: {Part2.solution(f)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
#Part 1: 157211394
#Took 0.0005 seconds

#Part 2: <run each pair in a new terminal>
#pair 1 of 10:  min =  881943038 (Took  818.8275 seconds)
#pair 2 of 10:  min = 3873623016 (Took   35.9264 seconds)
#pair 3 of 10:  min =  231522441 (Took  658.5484 seconds)
#pair 4 of 10:  min =  779172655 (Took  834.2236 seconds)
#pair 5 of 10:  min =  537129215 (Took 1401.6854 seconds)
#pair 6 of 10:  min =   50855035 (Took 1984.2461 seconds)
#pair 7 of 10:  min =  219189788 (Took  195.4743 seconds)
#pair 8 of 10:  min =  636993556 (Took 2937.6545 seconds)
#pair 9 of 10:  min = 2333639996 (Took    4.6707 seconds)
#pair 10 of 10: min =   75281325 (Took  813.6106 seconds)