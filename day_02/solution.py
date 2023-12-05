import re
import time

class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        sum = 0
        for line in iter(file_lines):
            split = re.split(":", line)
            game = re.sub("Game ", "", split[0])
            possible = Helper.check_game(re.split(";", split[1]))
            #print(f'{game}: {possible}')
            if possible:
               sum += int(game)
        return sum

class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        sum = 0
        for line in iter(file_lines):
            split = re.split(":", line)
            game = re.sub("Game ", "", split[0])
            power = Helper.get_power(re.split(";", split[1]))
            #print(f'{game}: {power}')
            sum += power
        return sum

class Helper:
    def check_game(pulls: list[str]) -> bool:    
        for pull in pulls:
            pairs = re.split(",", pull)
            for pair in pairs:                
                kvp = re.split(" ", pair)
                #print(f'color={kvp[2]}, number={kvp[1]}')
                if kvp[2] == "red" and int(kvp[1]) > 12:
                    return False                
                if kvp[2] == "green" and int(kvp[1]) > 13:
                    return False
                if kvp[2] == "blue" and int(kvp[1]) > 14:
                    return False
        return True
    
    def get_power(pulls: list[str]) -> int:
        min_red = 0
        min_green = 0
        min_blue = 0
        for pull in pulls:
            pairs = re.split(",", pull)
            for pair in pairs:                
                kvp = re.split(" ", pair)
                #print(f'color={kvp[2]}, number={kvp[1]}')
                if kvp[2] == "red":
                    min_red = max(min_red, int(kvp[1]))
                if kvp[2] == "green":
                    min_green = max(min_green, int(kvp[1]))
                if kvp[2] == "blue":
                    min_blue = max(min_blue, int(kvp[1]))
        #print(f'red={min_red}, green={min_green}, blue={min_blue}')
        return min_red * min_green * min_blue

tic = time.perf_counter()
#with open("sample.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()
print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
toc = time.perf_counter()
print(f"Took {time.perf_counter() - tic:0.4f} seconds")
#Part 1: 2505
#Part 2: 70265
#Took 0.0016 seconds