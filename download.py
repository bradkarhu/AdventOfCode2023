# requires https://github.com/scarvalhojr/aoc-cli

import os
import subprocess

for i in range(1, 26):
    dir_path = os.path.join(os.path.dirname(__file__), f'day_{i:02}')
    if os.path.exists(dir_path):
        input_path = os.path.join(dir_path, 'input.txt')
        if not os.path.exists(input_path):
            command = f'aoc download --year 2023 --day {i} --input-only --input-file {input_path}'
            subprocess.run(command, shell=True)        
        puzzle_path = os.path.join(dir_path, 'puzzle.md')
        if not os.path.exists(puzzle_path):
            command = f'aoc download --year 2023 --day {i} --puzzle-only --puzzle-file {puzzle_path}'
            subprocess.run(command, shell=True)