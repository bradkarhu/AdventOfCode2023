import time

class Part1:
    @staticmethod
    def solution(line: str) -> int:        
        return sum(Helper.hash(s) for s in line.split(','))

class Part2:
    @staticmethod
    def solution(line: str) -> int:
        boxes = []
        for _ in range(256): boxes.append([]) # init
        for s in line.split(','):
            if s[-1] == '-':
                a = s[:-1]
                box = boxes[Helper.hash(a)]
                index = Helper.get_index(box, a)
                if index >= 0: 
                    del box[index]
            else:
                a, lens = s.split('=')
                box = boxes[Helper.hash(a)]
                index = Helper.get_index(box, a)
                if index >= 0: 
                    box[index] = (a, lens)
                else: 
                    box.append((a, lens))
        #print(boxes)
        total = 0
        for i in range(len(boxes)):
            for j in range(len(boxes[i])):
                total += (i+1) * (j+1) * int(boxes[i][j][1])
        return total

class Helper:
    def hash(s: str) -> int:
        value = 0        
        for c in iter(s):
            value += ord(c)
            value *= 17
            value %= 256
        return value
    
    def get_index(box: list[tuple], a: str) -> int:
        for i in range(len(box)):
            if box[i][0] == a: return i
        return -1

tic = time.perf_counter()
#with open("sample.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read()
print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
#Part 1: 513158
#Part 2: 200277
#Took 0.0047 seconds