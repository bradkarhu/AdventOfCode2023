import functools
import time

# keywords:
# dynamic programming 
# memoization
# recursion with cache 

class Part1:    
    @staticmethod 
    def solution(lines: list[str]) -> int:
        total = 0
        for line in iter(lines):
            data, series = line.split()
            series_t = tuple(int(i) for i in series.split(','))
            total += DP.func(data, series_t, 0, 0, 0)
            #print(DP.func.cache_info())
            DP.func.cache_clear() # must reset it after each line            
        return total

class Part2: 
    @staticmethod # dynamic programming using memoization
    def solution(lines: list[str]) -> int:
        total = 0
        for line in iter(lines):
            data, series = line.split()
            data = '?'.join([data] * 5)
            series = ','.join([series] * 5)
            series_t = tuple(int(i) for i in series.split(','))
            total += DP.func(data, series_t, 0, 0, 0)
            DP.func.cache_clear() # must reset it after each line
        return total

class DP:
    @functools.lru_cache(maxsize=None)
    def func(data, series: tuple, i: int, si: int, num: int) -> int:
        """ 
        recurse over the data range and find all arrangements that match the series
        i: current position within the data list
        si: current position withn the series list
        num: current number of contiguous #s
        """
        if i == len(data): # past the end
            if si == len(series) and num == 0: # right number of series with no extra #s
                return 1
            if si == len(series) - 1 and num == series[si]: # finished off the last series
                return 1
            return 0 # this combination didn't match the series
        ans = 0
        # if '?', try both '#' and '.'
        if data[i] in ('#', '?'):
            # add a hash and keep on diggin'
            ans += DP.func(data, series, i + 1, si, num + 1)
        if data[i] in ('.', '?'):
            if num == 0: 
                # dots after dots and nothing to do
                ans += DP.func(data, series, i + 1, si, 0)
            elif si < len(series) and num == series[si]: 
                # move to next series if the last segment was a match
                ans += DP.func(data, series, i + 1, si + 1, 0)
        return ans

#with open("sample.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()
tic = time.perf_counter()
print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
#Part 1: 7169
#Part 2: 1738259948652
#Took 0.7744 seconds