from sys import argv

class Brick:
    def __init__(self, line: str, id) -> None:
        s1, s2 = line.split("~")
        p1 = [int(n) for n in s1.split(",")]
        p2 = [int(n) for n in s2.split(",")]
        self.x1 = min(p1[0], p2[0])
        self.x2 = max(p1[0], p2[0])
        self.y1 = min(p1[1], p2[1])
        self.y2 = max(p1[1], p2[1])
        self.z1 = min(p1[2], p2[2])
        self.z2 = max(p1[2], p2[2])
        self.id = id

    def is_supported(self, stack: dict) -> bool:
        z = self.z1 - 1
        for x in range(self.x1, self.x2 + 1):
            for y in range(self.y1, self.y2 + 1):
                if (x, y, z) in stack: 
                    return True
        return False
    
    def get_supporting_bricks(self, stack: dict) -> set:
        bricks = set()
        z = self.z2 + 1
        for x in range(self.x1, self.x2 + 1):
            for y in range(self.y1, self.y2 + 1):
                if (x, y, z) in stack: 
                    brick = stack.get((x, y, z))
                    bricks.add(brick.id)
        return bricks
    
    def is_supported_by_other_than(self, ignore, stack: dict) -> bool:
        z = self.z1 - 1
        for x in range(self.x1, self.x2 + 1):
            for y in range(self.y1, self.y2 + 1):
                if (x, y, z) in stack:
                    brick = stack.get((x, y, z))
                    if brick.id != ignore:
                        return True
        return False

def solve(lines: list[str]):
    bricks = parse(lines)
    bricks_sorted = sorted(bricks, key=lambda x: x.z1, reverse=True)
    bricks_by_id = { b.id: b for b in bricks }
    # store the stack as a dict of (x,y,z) = Brick
    stack = {}
    while bricks_sorted:
        b = bricks_sorted.pop()        
        # check if any voxel under a brick belongs to the stack (z=0 is all part of stack)
        if b.z1 == 1 or b.is_supported(stack):
            # add it to the stack, remove from list of falling
            #print(f'{b.id} added to the stack')
            for x in range(b.x1, b.x2 + 1):
                for y in range(b.y1, b.y2 + 1):
                    for z in range(b.z1, b.z2 + 1):
                        stack[(x, y, z)] = b
        else:
            # drop z by 1 and keep it in the queue
            #print(f'{b.id} continues to fall')
            b.z1 -= 1
            b.z2 -= 1
            bricks_sorted.append(b)
    num = 0
    for id, brick in bricks_by_id.items():
        can_disintegrate = True
        for other in brick.get_supporting_bricks(stack):
            if not bricks_by_id[other].is_supported_by_other_than(id, stack):
                can_disintegrate = False
        if can_disintegrate: num += 1
    print(num)
    
def parse(lines: list[str]) -> list[Brick]:
    bricks = []
    num = 0
    for line in lines:
        id = num #chr(65 + num)
        bricks.append(Brick(line, id))
        num += 1
    return bricks

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)