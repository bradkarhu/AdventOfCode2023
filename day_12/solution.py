import itertools
import re
import time

class Part1:
    @staticmethod
    def solution(lines: list[str]) -> int:
        total_arrangements = 0
        for line in iter(lines):
            s = line.split()
            data = s[0]
            #print(data)
            series_list = [int(i) for i in s[1].split(',')]
            #print(series)
            arrangements = 0
            unknowns = [i for i, c in enumerate(data) if c == '?']
            #print(unknowns)
            combos = itertools.product(['.', '#'], repeat=len(unknowns))
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

class Part2:
    @staticmethod
    def solution(lines: list[str]) -> int:
        total_arrangements = 0
        for line in iter(lines):
            s = line.split()
            data = s[0] + '?' + s[0] + '?' + s[0] + '?' + s[0] + '?' + s[0]
            series = s[1] + ',' + s[1] + ',' + s[1] + ',' + s[1] + ',' + s[1]
            print(data)
            series_list = [int(i) for i in series.split(',')]
            #print(series)
            arrangements = 0
            unknowns = [i for i, c in enumerate(data) if c == '?']
            #print(unknowns)
            combos = itertools.product(['.', '#'], repeat=len(unknowns))
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

class Helper:
    def print_lines(lines: list[str]):
        for line in iter(lines):
            print(line)
    
    def write_lines(lines: list[str], filename: str):      
        with open(filename, "w") as file:
            file.writelines("\r\n".join(lines))

tic = time.perf_counter()
#with open("sample.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()
print(f"Part 1: {Part1.solution(f)}")
#print(f"Part 2: {Part2.solution(f)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
#Part 1: 7169
#Took 9.7403 seconds