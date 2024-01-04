from os import path
from sys import argv
from subprocess import run

if len(argv) < 2:
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

day = argv[1]
part = argv[2]

dir_path = path.join(path.dirname(__file__), f'day_{int(day):02}')
script_path = path.join(dir_path, f'{part}.py')
input_path = path.join(dir_path, 'input.txt')

command = f'time python3 {script_path} {input_path}'
p = run(command, shell=True, executable='/bin/zsh', capture_output=True, text=True)
# stderr: 'python3 <file>  0.63s user 0.03s system 99% cpu 0.661 total'
_, _, u_sec, _, s_sec, _, cpu, _, t_sec, _ = p.stderr.split()
ans = p.stdout.splitlines()[0]

print(f'AOC 2023 Day {day} -- Part {part}')
print(ans)
print(f'Took {t_sec} seconds')
print("")