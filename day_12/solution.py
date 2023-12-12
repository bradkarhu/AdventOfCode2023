import itertools
import time

class Part1:
    @staticmethod # brute force
    def solution(lines: list[str]) -> int:
        total_arrangements = 0
        for line in iter(lines):
            data, series = line.split()
            series_list = [int(i) for i in series.split(',')]
            unknowns = [i for i, c in enumerate(data) if c == '?']
            combos = itertools.product(['.', '#'], repeat=len(unknowns))
            arrangements = 0
            for combo in iter(combos):
                data_list = list(data)
                group_list = []
                count = 0
                for i in range(len(unknowns)):
                    data_list[unknowns[i]] = combo[i]
                for i in range(len(data_list)):
                    if data_list[i] == '#': 
                        count += 1
                    elif count > 0:
                        group_list.append(count)
                        count = 0
                if count > 0: group_list.append(count)
                if series_list == group_list:
                    arrangements += 1
            total_arrangements += arrangements
        return total_arrangements
    
    @staticmethod # dynamic programming
    def optimized(lines: list[str]) -> int:
        total_arrangements = 0
        for line in iter(lines):
            data, series = line.split()
            series_list = [int(i) for i in series.split(',')]
            arrangements = DP.func(data, series_list, 0, 0, 0)
            total_arrangements += arrangements
            #print(f'{line} => {arrangements}')
            DP.cache.clear() # must reset it after each line
        return total_arrangements

class Part2: 
    @staticmethod # dynamic programming
    def solution(lines: list[str]) -> int:
        total_arrangements = 0
        for line in iter(lines):
            data, series = line.split()
            data = '?'.join([data, data, data, data, data])
            series = ','.join([series, series, series, series, series])
            series_list = [int(i) for i in series.split(',')]
            arrangements = DP.func(data, series_list, 0, 0, 0)
            total_arrangements += arrangements
            #print(f'{line} => {arrangements}')
            DP.cache.clear() # must reset it after each line
        return total_arrangements

class DP:
    cache = {} # (i, si, num) => number of arrangements
        
    def func(data: str, series: list[int], i: int, si: int, num: int):
        """ 
        recurse over the data range and find all arrangements that match the series
        i: current position within the data list
        si: current position withn the series list
        num: current number of contiguous #s
        """        
        key = (i, si, num)
        DP.cache_hits_and_misses += 1 # metrics
        if key in DP.cache: 
            DP.cache_hits += 1 # metrics
            return DP.cache[key] # DP at work!
        if i == len(data): # past the end
            if si == len(series) and num == 0: # right number of series with no extra #s
                return 1
            if si == len(series) - 1 and num == series[si]: # finished off the last series
                return 1
            return 0 # this combination didn't match the series
        arrangements = 0
        # if '?', try both '#' and '.'
        if data[i] in ('#', '?'):
            # add a hash and keep on diggin'
            arrangements += DP.func(data, series, i + 1, si, num + 1)
        if data[i] in ('.', '?'):
            if num == 0: 
                # dots after dots and nothing to do
                arrangements += DP.func(data, series, i + 1, si, 0)
            elif si < len(series) and num == series[si]: 
                # move to next series if the last segment was a match
                arrangements += DP.func(data, series, i + 1, si + 1, 0)
        DP.cache[key] = arrangements
        return arrangements

    # metrics
    cache_hits = 0
    cache_hits_and_misses = 0

#with open("sample.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()
tic = time.perf_counter()
print(f"Part 1: {Part1.solution(f)} (brute force)")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
#Part 1: 7169 (brute force)
#Took 9.6440 seconds
tic = time.perf_counter()
print(f"Part 1: {Part1.optimized(f)} (hit ratio: {100*(DP.cache_hits/DP.cache_hits_and_misses):0.2f}%)")
DP.cache_hits = 0
DP.cache_hits_and_misses = 0
print(f"Part 2: {Part2.solution(f)} (hit ratio: {100*(DP.cache_hits/DP.cache_hits_and_misses):0.2f}%)")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
#Part 1: 7169 (hit ratio: 4.65%)
#Part 2: 1738259948652 (hit ratio: 5.25%)
#Took 0.6811 seconds