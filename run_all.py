from os import path
from subprocess import run

print("| Day | Part 1 | Part 2 |")
print("| --- | --- | --- |")

for i in range(1, 26):
    dir_path = path.join(path.dirname(__file__), f'day_{i:02}')
    if path.exists(dir_path):
        input_path = path.join(dir_path, 'input.txt')
        values = [ '---', '---' ]
        for part in range(1, 3):
            script_path = path.join(dir_path, f'{part}.py')
            if path.exists(input_path) and path.exists(script_path):
                command = f'python3 {script_path} {input_path}'
                p = run(command, shell=True, capture_output=True, text=True)
                values[part - 1] = p.stdout.splitlines()[0]
        print(f"| {i} | {values[0]} | {values[1]} |")