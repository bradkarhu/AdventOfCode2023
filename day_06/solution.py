from math import sqrt
import time

class Part1:
    @staticmethod
    def solution(lines: list[str]) -> int:
        times = [int(s) for s in lines[0].split()[1:]]
        dists = [int(s) for s in lines[1].split()[1:]]
        total = 1
        for index in range(len(times)):
            ways2win = 0
            totaltime = times[index]
            winningdistance = dists[index]
            for hold in range(1, totaltime):
                traveltime = totaltime - hold
                distance = hold * traveltime
                if distance > winningdistance: 
                    ways2win += 1
            total *= ways2win
        return total

class Part2:
    @staticmethod
    def solution(lines: list[str]) -> int:
        tt_s = lines[0].replace(" ", "").split(":")[1]
        dd_s = lines[1].replace(" ", "").split(":")[1]
        tt = int(tt_s)
        dd = int(dd_s)
        factor = pow(10, len(tt_s))
        mid = int(tt / 2)
        min = mid
        max = mid
        while factor >= 1:
            for t in range(min, min - (factor * 10), factor * -1):
                if t * (tt - t) > dd and min > t: min = t
            for t in range(max, max + (factor * 10), factor):
                if t * (tt - t) > dd and max < t: max = t
            factor = int(factor / 10)
        return max - min + 1

    @staticmethod
    def shortcut(lines: list[str]) -> int:
        tt_s = lines[0].replace(" ", "").split(":")[1]
        dd_s = lines[1].replace(" ", "").split(":")[1]
        a = 1
        b = int(tt_s)
        c = int(dd_s)
        # solve using the quadratic formula
        t1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
        t2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
        return int(max(t1, t2) - min(t1, t2))

#class Helper:

tic = time.perf_counter()
#with open("sample.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()
print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
print(f"Part 2: {Part2.shortcut(f)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.5f} seconds")
#Part 1: 771628
#Part 2: 27363861
#Took 0.0001 seconds