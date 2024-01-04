from math import sqrt
import sys

def solve(lines: list[str]):
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
    print(total)

with open(sys.argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)