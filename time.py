import os
import sys
import subprocess

if len(sys.argv) < 2:
    print("")
    print("Script to get the runtime of each solution")
    print("")
    print("Usage: time <DAY> <PART>")
    print("")
    print("Arguments:")
    print("  <DAY>  Puzzle day [1 thru 25]")
    print("  <PART> Puzzle part [1 or 2]")
    print("")
    exit()

day = sys.argv[1]
part = sys.argv[2]

dir_path = os.path.join(os.path.dirname(__file__), f'day_{int(day):02}')
script_path = os.path.join(dir_path, f'{part}.py')
input_path = os.path.join(dir_path, 'input.txt')

#command = f'/bin/zsh -c "time python3 {script_path} {input_path}"'
#os.system(command)

command = f'python3 -m cProfile {script_path} {input_path}'
p = subprocess.run(command, shell=True, capture_output=True, text=True)
lines = p.stdout.splitlines()
ans = lines[0]
seconds = lines[1].split()[-2]

print(f'AOC 2023 Day {day} -- Part {part}')
print(ans)
print(f'Took {seconds} seconds')
print("")

with open("profile.txt", "w") as file:
    file.writelines("\r\n".join(lines[1:]))