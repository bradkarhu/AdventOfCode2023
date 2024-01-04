from os import path
from subprocess import run

print("| Day | p1 cpu | p1 sec | p2 cpu | p2 sec |")
print("| --- | --- | --- | --- | --- |")
cpu_total = [ [], [] ]
sec_total = [ 0, 0 ]
for i in range(1, 26):
    dir_path = path.join(path.dirname(__file__), f'day_{i:02}')
    if path.exists(dir_path):
        input_path = path.join(dir_path, 'input.txt')
        cpu_values = [ '---', '---' ]
        sec_values = [ '---', '---' ]
        for part in range(1, 3):
            script_path = path.join(dir_path, f'{part}.py')
            if path.exists(input_path) and path.exists(script_path):
                command = f'time python3 {script_path} {input_path}'
                p = run(command, shell=True, executable='/bin/zsh', capture_output=True, text=True)
                # stderr: 'python3 <file> 0.63s user 0.03s system 99% cpu 0.661 total'
                _, _, u_sec, _, s_sec, _, cpu, _, t_sec, _ = p.stderr.split()
                seconds = max(0.001, float(t_sec))
                cpu_values[part - 1] = cpu
                sec_values[part - 1] = seconds
                cpu_total[part - 1].append(int(cpu[:-1]))
                sec_total[part - 1] += seconds
        print(f"| {i} | {cpu_values[0]} | {sec_values[0]} | {cpu_values[1]} | {sec_values[1]} |")
cpu_total_p1 = sum(cpu_total[0]) // len(cpu_total[0])
cpu_total_p2 = sum(cpu_total[1]) // len(cpu_total[1])
print(f"| Total | {cpu_total_p1}% | {sec_total[0]:0.4f} | {cpu_total_p2}% | {sec_total[1]:0.4f} |")