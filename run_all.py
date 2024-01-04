import os
import subprocess

print("| Day | Part 1 | Part 2 |")
print("| --- | --- | --- |")

for i in range(1, 26):
    dir_path = os.path.join(os.path.dirname(__file__), f'day_{i:02}')
    if os.path.exists(dir_path):
        input_path = os.path.join(dir_path, 'input.txt')
        values = [ '---', '---' ]
        for part in range(1, 3):
            script_path = os.path.join(dir_path, f'{part}.py')
            if os.path.exists(input_path) and os.path.exists(script_path):
                command = f'python3 {script_path} {input_path}'
                p = subprocess.run(command, shell=True, capture_output=True, text=True)
                lines = p.stdout.splitlines()
                ans = lines[0]
                values[part - 1] = ans
        print(f"| {i} | {values[0]} | {values[1]} |")