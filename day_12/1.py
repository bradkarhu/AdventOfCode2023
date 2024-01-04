import itertools
import sys

def solve(lines: list[str]):
    total = 0
    for line in iter(lines):
        data, series = line.split()
        series_list = [int(i) for i in series.split(',')]
        arrangements = func(data, series_list, 0, 0, 0)
        total += arrangements
        #print(f'{line} => {arrangements}')
        cache.clear() # must reset it after each line
    print(total)

cache = {} # (i, si, num) => number of arrangements

def func(data: str, series: list[int], i: int, si: int, num: int):
    """ 
    recurse over the data range and find all arrangements that match the series
    i: current position within the data list
    si: current position withn the series list
    num: current number of contiguous #s
    """        
    key = (i, si, num)
    if key in cache: 
        return cache[key] # DP at work!
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
        arrangements += func(data, series, i + 1, si, num + 1)
    if data[i] in ('.', '?'):
        if num == 0: 
            # dots after dots and nothing to do
            arrangements += func(data, series, i + 1, si, 0)
        elif si < len(series) and num == series[si]: 
            # move to next series if the last segment was a match
            arrangements += func(data, series, i + 1, si + 1, 0)
    cache[key] = arrangements
    return arrangements

with open(sys.argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)